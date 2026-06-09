# Public Source Corpus

This skill is based on public or package-facing sources, not private infrastructure notes.

## TweetClaw Sources

- TweetClaw repository: https://github.com/Xquik-dev/tweetclaw
- TweetClaw README: install, credential modes, optional tools, OpenClaw approval model, commands, monitor behavior, and use cases
- TweetClaw bundled skill: `skills/tweetclaw/SKILL.md`
- OpenClaw setup guide: `docs/openclaw-setup.md`
- Agent workflow guide: `docs/agent-workflows.md`
- npm package metadata: `@xquik/tweetclaw`

## OpenClaw Sources

- OpenClaw docs home: https://docs.openclaw.ai
- CLI plugin install and update docs: https://docs.openclaw.ai/cli/plugins.md
- Tool plugin docs: https://docs.openclaw.ai/tools/plugin.md
- Manifest docs: https://docs.openclaw.ai/plugins/manifest.md
- Permission request docs: https://docs.openclaw.ai/plugins/plugin-permission-requests.md
- Agent tools docs: https://docs.openclaw.ai/plugins/agent-tools.md
- SDK entrypoint and runtime docs: https://docs.openclaw.ai/plugins/sdk-entrypoints.md and https://docs.openclaw.ai/plugins/sdk-runtime.md
- Install override docs: https://docs.openclaw.ai/plugins/install-overrides.md
- ClawHub publishing and skill format docs: https://docs.openclaw.ai/clawhub/publishing.md and https://docs.openclaw.ai/clawhub/skill-format.md
- CLI skills docs: https://docs.openclaw.ai/cli/skills.md
- Debugging docs: https://docs.openclaw.ai/help/debugging.md

## Xquik Sources

- Xquik app: https://xquik.com
- Xquik dashboard: https://dashboard.xquik.com
- Xquik docs: https://docs.xquik.com
- API reference: https://docs.xquik.com/api-reference/overview
- Billing guide: https://docs.xquik.com/guides/billing

## Corpus Notes

The reusable patterns in this skill come from:

- Explicit npm install and pinned update guidance
- Runtime inspection checks
- Optional tool exposure plus per-call approval
- Explore-first endpoint discovery
- Account-backed vs MPP read-only mode separation
- Dashboard-only boundaries
- Private-data, paid-work, recurring-work, and write-action approval gates
