# Cheatsheet

## Weekly Template (Ch01, Ch03)
| Slot | Activity |
|---|---|
| Monday morning | Own content: shooting every 2 weeks 8:00–12:00 (recurring), cover/b-roll material, briefing the editor |
| Monday afternoon | Clients, or a personal side project (e.g. a peer podcast) |
| Tuesday–Thursday | Client work: design, training, consultations, calls and email |
| Thursday | Editing the long-form piece so it's ready for the following Monday |
| Friday | Write next week's content, plan next week's slots; calm/light tasks in the afternoon (or on travel days) |
| Weekend | Off; at most Saturday morning to catch up on content |
| Daily stop | Mon–Fri until **18:00**, rarely exceeded |
| Planning moment | Sunday evening or Monday; weekly goals when projects can be scheduled, day-by-day for small-task periods |
| Peak split seen | ~2 days/week social content, 3 days clients |

## Service Formats (Ch01)
| Service | Format |
|---|---|
| Client design projects | Decks (corporate, convention/event, numbers-heavy report), showcase websites (with a developer partner), templates |
| Deck duration | ~**1 month** part-time (immersion → style research → paper sketches → first version → revisions) |
| Tight deadline | Workable (~2 weeks for a convention deck) only with every day on that single project |
| Consultation | **1–1.5 h** max; slides received in advance; fixed live; client leaves with a before/after file |
| Training | **2, 3 or 4 h** compact formats up to multi-day programmes; online or in person (in person worth more; cap travel) |
| Online course production | Pitch to a platform (what you do, results, proposed course), then write and record to its guidelines |
| Content creation | A project where you are the client |
| Hour packages | Sold "on consumption" (e.g. 10 h), tracked in the hour tracker |
| Out of scope | Refer to other designers (e.g. logos/brand identity) |

### Quote Phases (Ch01)
1. Content immersion 2. Style research 3. Revision rounds (first version is never the good one).
Discovery questions: audience, occasion, deadline, number of slides, brand assets, who edits the file later; probe extra decks, animations, numbers-heavy sections.

### Client Communication Rules (Ch01)
| Rule | Practice |
|---|---|
| Official channel | Email; avoid WhatsApp and voice messages; move Instagram DMs to email |
| Phone | Your choice to share |
| Working hours | Decide (e.g. Mon–Fri until 18:00) and state at onboarding |
| Feedback | Explain the *why* of each choice; aim for clients who trust you |
| Best-fit clients | Those who come from your content |
| Print-only jobs | Conscious exceptions if errors cause anxiety |
| Many contributors | Merge selected ideas, credit authors by name |

### Delegation (Ch01, Ch03, Ch04)
| Task | Delegate to |
|---|---|
| Fiscal/admin (taxes, contributions, e-invoicing) | Accountant, from day one |
| Footage editing | Editor with a set budget |

## Notion Databases, Properties, Views, Statuses (Ch02)

### Minimum Workspace
| Database | Properties | Views |
|---|---|---|
| **Projects** (hub) | Name; Client (Relation → Clients, limit 1, both sides); Status (Not started / In progress / Done); Start–End date (d/m/y, 24 h); Budget (Number, €, footer Sum); Notes (relation back); footer Count all on Name | Overview (table, all); Status (board by Status, coloured columns); Gantt (timeline, zoom **Quarter**); Revenue (name, client, budget; filter active/done) |
| **Clients** | Name/company; Contact (Email); Status; Projects (auto from relation) | — |
| **Notes** | Name; Date (Created time, d/m/y 24 h); Project (Relation → Projects, many allowed) | Sorted by date descending; Linked view inside each project filtered Project = this |

### Advanced Workspace
| Area / Database | Key content |
|---|---|
| Dashboard areas | **Freelancing** (projects, CRM, invoices, hour tracker, contacts, notes, VAT-number docs); **Personal branding** (content, own projects); **Personal** (expenses, habits, quotes) |
| Dashboard rule | Embedded preview only for databases checked constantly (e.g. unpaid invoices); others as links |
| Project statuses | Briefing → To start → Design → **Feedback** → Development → Ongoing → completed group: **To invoice** / Archived / Deleted |
| Project properties | Description, Client, Timing, Budget, Total hours, Hours done, Hours %, Hours remaining, **Energy** (Low/High), Type (multi-select), Quote, Invoices (relation), Year (formula from timing); Tracker and Notes as page sections |
| Project views | Gantt, Pipeline (kanban by phase), current year with revenue forecast, previous year, All grouped by year |
| CRM statuses | Call → Quote → Awaiting reply → Client → Lost; plus **Past clients** |
| CRM properties | Status, contact (email/Instagram), industry, website, request, dated step timeline, to-do, forecast revenue, linked projects, linked invoices, created time |
| Contacts | Profession (multi-select), email, phone, portfolio link |
| Notes tags | Travel, personal project, first contacts, outlines, scripts |
| Invoices | Number; issue date; **cash-in date**; Year from cash-in; client; linked projects; status (To issue/send, To collect, Paid); automatic amount (rollup) + manual amount (stamp duty, deposits); notes |
| Content | One database for all platforms; views Calendar, per-platform, Ideas by series, **Pipeline** (To write → To design → To record → To edit), long-form list; properties platform (relation), type, series, tags, status, created date, Sponsored (checkbox) |
| Personal | Expense tracker (categories), habit tracker (checkboxes, progress ring), saved quotes |

### Four Schematisation Questions (Ch02)
1. Which databases? 2. How related? 3. Which properties? 4. Which views (what must I see at first glance)?

## Hour Tracker Formulas (Ch02, Ch03)
| Field | Definition |
|---|---|
| Tracker DB | Task (title), Start (date+time, 24 h), End (date+time), Time (formula), Project (Relation, **limit 1**) |
| Time | `dateBetween(prop("End"), prop("Start"), "minutes") / 60` |
| Don't use | `"hours"`: rounds 16:00–16:30 to 1 instead of 0.5 |
| Total hours | Number, set manually from budget and available time |
| Hours done | Rollup → Tracker → Time → **Sum** |
| Hours remaining | `prop("Total hours") - prop("Hours done")` |
| Hours % | `round(prop("Hours done") / prop("Total hours") * 100) / 100`, shown as Percent with bar |
| Overrun | Hours % > 100% → talk to the client |
| View filters | By **End** date: Today (this day), Week (this week), **Yesterday** |
| Test values | 8:00–10:00 → 2; 14:00–14:30 → 0.5; 3 h on 10 h → 7 remaining, 30% |

Notion syntax is the classic formula syntax: verify against the current version.

## Calendar & Block Rules (Ch03)
| Rule | Value |
|---|---|
| Calendars as labels | One per area: default (calls), Administration, Content Creation, Family (shared), Training, Meeting, Personal, Project, Selfcare, Task (+ undeletable Reminders) |
| Colour | Custom hex per calendar (three-dot menu → + Add custom colour); never recolour single events |
| Block sizes | 1, 2, 3 or 4 h; typical **4 h**; design **3–4 h** on one project |
| Goal | Every block gets a Google Task (partial or deliverable-based) |
| Buffer | ~15 min (event ends 9:45 → next starts 10:00); don't schedule every break |
| Energy mapping | High-energy work in your best hours (often mornings), calls in the afternoon, calm tasks on draining days |
| Batching | Record 2–3 content pieces in a row |
| Recurring event | Does not repeat → Custom → every 2 weeks → End never / on date / after N |
| Micro-tasks | Paper notebook, cleared at day end; also records what you did |
| Leftovers | Move to tomorrow without guilt |
| Energy per project | Two Lows overlap fine; avoid two Highs |
| Start dates | Check the Quarter Gantt for overlaps first |

### Morning Routine Example (Ch03)
Cold water on the face → glass of water → 5 min breathing → stretching + 10 push-ups → journal on the previous day.

## Tools & Workspace (Ch04)
| Job | Tool |
|---|---|
| Email (multi-account) | Spark |
| Projects, hours, clients, invoices, content | Notion (free plan suffices) |
| Blocks and goals | Google Calendar + Google Tasks |
| Shared docs, backup | Google Drive |
| Wireframes, storyboards | iPad Notes (synced) |
| Inspiration | Behance, Dribbble, Pinterest (one board per project), Awwwards for web |
| Web design | Adobe XD → Figma |
| Decks | Keynote (favourite), PowerPoint (most requested), Google Slides |
| Screen recording | Screen Studio instead of OBS; iPhone on a desk tripod |

| Workspace item | Value |
|---|---|
| Sit-stand desk | e.g. 180×80 cm top, 58–123 cm height range, stored presets |
| Monitor | 27" (~10 kg may need its own stand), light bar for dark afternoons |
| Acoustics | Heavy theatre curtain on T-stands |
| Recording gear | Camera and softboxed LED panel left set up |
| Ergonomics | Laptop + monitor + right trackpad → wrist pain: close the laptop; chair with lumbar curve |

## Yearly Review Checklist (Ch04)
- [ ] Last year's two goals written, met or not
- [ ] One personal/wellbeing goal for the year
- [ ] One revenue goal: beat last year by any amount
- [ ] 4–6 main projects: liked, went wrong, one lesson each
- [ ] Channels reviewed: growth, clients brought, time cost
- [ ] "Why" document re-read and compared with behaviour
- [ ] Costs named (burnout, no breaks, isolation)
- [ ] Resolutions set
- [ ] Goal hit early → pause, recharge, rethink

### Monthly Notion Maintenance (Ch02)
- [ ] Archive Done projects; move silent leads to Lost / Past clients
- [ ] Check To collect invoices; update cash-in dates
- [ ] Remove unused properties or add them to onboarding
- [ ] Review the Energy mix before accepting work
- [ ] Add features only when they answer an existing question

## Italy-Specific Notes (Ch01) — orientation only, not tax advice
| Item | Note |
|---|---|
| **[Italy]** Testing phase | *Prestazione occasionale* / *ritenuta d'acconto* while studying (~3 years here) |
| **[Italy]** Partita IVA | Open when work becomes regular |
| **[Italy]** Regime forfettario | Start-up rate 5% for the first 5 years, then 15% |
| **[Italy]** Cash basis | Income counts on the cash-in date (*incasso*): a December invoice paid in January is next year's income → compute invoice Year from cash-in |
| **[Italy]** Stamp duty | *Marca da bollo* added manually (manual amount field) |
| **[Italy]** E-invoicing | Mandatory, usually in the accountant's portal |
| **[Italy]** INPS, ATECO | Confusing at first: what the accountant is for |
| First-year target | Prudent and reachable, based on real living costs |
