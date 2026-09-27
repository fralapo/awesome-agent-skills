#!/usr/bin/env python3
"""Minimal client for the real JEV model via OpenRouter's Decisions API.

Stdlib only, no dependencies. See ../references/api.md for the full schema.

Usage:
    jev_client.py --state "..." --noul key="instructions" [--noul ...]
                                 --choice key="instructions:optA,optB,optC"
                                 --score key="instructions:levelA,levelB,levelC"
    jev_client.py request.json          # {"state": ..., "questions": {...}}
    jev_client.py -                     # read the same JSON from stdin
    jev_client.py items.jsonl [-w N]    # one request per line, run in parallel,
                                        # prints one result per line, same order

Python:
    decide(state, questions)            -> response dict (raises JevError)
    decide_many([{"state":..,"questions":..}, ...], workers=8)
                                        -> list of response dicts or {"error": msg}

Env:
    OPENROUTER_API_KEY          required
    OPENROUTER_API_KEY_BACKUP   optional — used if the primary key is out of
                                credit or unauthorized (401/402/403)
    JEV_MODEL                   default "typesafe/jev-1.13"
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ENDPOINT = "https://openrouter.ai/api/alpha/decisions"
DEFAULT_MODEL = "typesafe/jev-1.13"
FAILOVER_CODES = {401, 402, 403}
RETRY_CODES = {429, 500, 502, 503, 504}
MAX_RETRIES = 3


class JevError(Exception):
    pass


def _post(api_key, payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    for attempt in range(MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code not in RETRY_CODES or attempt == MAX_RETRIES:
                raise
        except urllib.error.URLError:
            if attempt == MAX_RETRIES:
                raise
        time.sleep(0.5 * 2 ** attempt)


def decide(state, questions, model=None):
    primary = os.environ.get("OPENROUTER_API_KEY")
    backup = os.environ.get("OPENROUTER_API_KEY_BACKUP")
    if not primary:
        raise JevError("OPENROUTER_API_KEY not set. Export it before calling JEV.")

    payload = {
        "model": model or os.environ.get("JEV_MODEL", DEFAULT_MODEL),
        "state": state,
        "questions": questions,
    }

    try:
        return _post(primary, payload)
    except urllib.error.HTTPError as e:
        if e.code in FAILOVER_CODES and backup:
            try:
                return _post(backup, payload)
            except urllib.error.HTTPError as e2:
                detail = e2.read().decode("utf-8", errors="replace")
                raise JevError(f"JEV request failed on both keys ({e2.code}): {detail}")
        detail = e.read().decode("utf-8", errors="replace")
        raise JevError(f"JEV request failed ({e.code}): {detail}")
    except urllib.error.URLError as e:
        raise JevError(f"Could not reach OpenRouter: {e.reason}")


def decide_many(requests, workers=8):
    def one(r):
        try:
            return decide(r["state"], r["questions"], r.get("model"))
        except JevError as e:
            return {"error": str(e)}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(one, requests))


def _parse_inline_question(spec, qtype):
    # key="instructions" or key="instructions:opt1,opt2,opt3"
    key, _, rest = spec.partition("=")
    instructions, _, options_csv = rest.partition(":")
    q = {"type": qtype, "instructions": instructions}
    if options_csv:
        options = [o.strip() for o in options_csv.split(",") if o.strip()]
        if qtype == "score":
            q["criteria"] = options
        else:
            q["criteria"] = {o: o for o in options}
    return key, q


def _cli():
    argv = sys.argv[1:]
    if not argv:
        raise SystemExit(__doc__)

    if argv[0].endswith(".jsonl"):
        workers = int(argv[argv.index("-w") + 1]) if "-w" in argv else 8
        with open(argv[0], "r", encoding="utf-8") as f:
            requests = [json.loads(line) for line in f if line.strip()]
        for result in decide_many(requests, workers):
            print(json.dumps(result))
        return

    if argv[0] == "-":
        payload = json.load(sys.stdin)
        result = decide(payload["state"], payload["questions"], payload.get("model"))
        print(json.dumps(result, indent=2))
        return

    if not argv[0].startswith("--"):
        with open(argv[0], "r", encoding="utf-8") as f:
            payload = json.load(f)
        result = decide(payload["state"], payload["questions"], payload.get("model"))
        print(json.dumps(result, indent=2))
        return

    state = None
    questions = {}
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--state":
            state = argv[i + 1]
            i += 2
        elif arg in ("--noul", "--choice", "--score"):
            qtype = arg[2:]
            key, q = _parse_inline_question(argv[i + 1], qtype)
            questions[key] = q
            i += 2
        else:
            raise SystemExit(f"Unknown argument: {arg}")

    if state is None or not questions:
        raise SystemExit("Need --state and at least one --noul/--choice/--score")

    result = decide(state, questions)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        _cli()
    except JevError as e:
        raise SystemExit(str(e))
