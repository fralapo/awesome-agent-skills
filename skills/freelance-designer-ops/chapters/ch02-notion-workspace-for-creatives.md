# Chapter 02: A Notion Workspace for Creatives

## Core Idea
Notion feels hard not because it has too many functions but because it is chaotic for anyone who does not yet know what they need — the same is true of PowerPoint or any software: knowing the features is useless without knowing your requirements. So the workspace is designed before it is built: **Learn → Schematise → Apply**. Learn from templates and other people's systems (to understand *why* they are structured that way, not to duplicate them); schematise on paper by answering four questions (which databases, which relations, which properties, which views); then build in the software. Notion's logic is a matryoshka of pages inside pages, where any page can be a database (rows = items, columns = properties) shown through multiple views (table, board, timeline, calendar, list, gallery). The power lies in **relations** (connecting databases) and **rollups** (aggregating values from a related database, e.g. summing tracked hours per project). A freelancer's minimum viable workspace is three related databases — Projects (the hub), Clients, Notes — each with one view per *question you need answered at a glance*. Over time it grows into a full system: projects with explicit statuses and hour budgets, a CRM pipeline, an hour tracker, invoices tracked by cash-in date, contacts for collaborators, and a single content database for all social channels. The system is never finished: properties turn out useless, new needs and features appear.

## Frameworks Introduced
**Learn → Schematise → Apply**: three steps before and during the build.
When to use: any new organisational tool (Notion, Airtable, a project tracker for an agency).

**The four schematisation questions**: 1) Which databases do I need? (imagine the menu of your home page) 2) How are they related? 3) Which properties does each need? 4) Which views and layouts — i.e. what must I grasp at first glance?
When to use: on paper or tablet notes, before opening the software.

**One view per goal**: every view exists to answer one question; show only the properties that serve that question, filter and sort for it. If the focus is dates, use a Timeline, not a table.
When to use: whenever adding a view.

**Generic properties over per-type databases**: instead of one database per service (training, decks, websites) with all its process steps, keep one Projects database with generic properties and statuses that fit every service.
When to use: when you run heterogeneous project types alone.

**Yourself as a client**: create a project for your own content creation (client = you) so its hours are tracked like client work.
When to use: when content or personal projects silently eat billable time.

## Rules & Practices
Logic and building blocks:
- Matryoshka logic: pages contain pages; a note "belongs" to the Notes macro-page and is only *linked* to a project.
- A new database row is an item; it becomes a page once you add content inside it.
- Property types used: Title, Status, Select/Multi-select (tags), Date, Number, Email, Created time, Formula, Relation, Rollup, Checkbox.
- Filters can use any property (type, date range…); sorting e.g. by start date, most recent first.
- Column footers can calculate: **Sum** on budget (total revenue), **Count all** on the name column (number of projects).

Minimum workspace (3 databases):
- **Projects** (main hub): Name; Client (Relation → Clients, limit 1, shown on both sides); Status (Not started / In progress / Done); Start–End date (day/month/year, 24-hour time); Budget (Number, € format, Sum in footer); Notes (relation back from Notes).
- **Clients**: Name/company; Contact (Email); Status (to see if active or where they are in onboarding); Projects (filled automatically by the relation).
- **Notes**: Name; Date (Created time, day/month/year 24 h); Project (Relation → Projects; several projects per note allowed); sort descending by date.
- Purpose of each: Projects = what is active now *and* an archive; Clients = full list incl. past clients you can recontact; Notes = history of everything said in meetings.

Projects views:
- **Overview**: table, all properties.
- **Status**: Board grouped by Status, coloured columns, cards show client + status; dragging a card changes its status.
- **Gantt**: Timeline by date, table on the left with name + client, status visible on bars; zoom **Quarter** to see ~3–4 months and spot overlapping projects.
- **Revenue**: table showing only name, client, budget; filter to active or completed projects (exclude deleted/never-started ones, or the total is not truthful).

Advanced workspace (a working freelancer's setup, used solo for ~2 years):
- Three areas on the dashboard: **Freelancing** (projects, CRM, invoices, hour tracker, contacts, notes, VAT-number info and documents), **Personal branding** (content creation, personal projects such as own site, course, guide), **Personal** (expenses, habits, quotes).
- Only databases you check constantly get an embedded preview on the dashboard (e.g. unpaid invoices); the others are just links.
- **Project statuses**: Briefing → To start (all material received, not started) → Design → Feedback (waiting for the client) → Development (website handed to the developer; you might still be needed) → Ongoing (recurring work such as school lessons September–June) → completed group: To invoice / Archived / Deleted.
- **Project properties**: description, Client (relation), Timing (start–end), Budget, Total hours (set manually from budget and available time), Hours done (rollup from Tracker), Hours % , Hours remaining, **Energy** (Low/High — too many High projects means decline the next one), Type (multi-select; many types if you like variety), Quote, Invoices (relation), Year (formula from the timing dates, used in filters); Tracker and Notes shown as expanded page sections.
- **Project views**: Gantt (can I start a new project on day X?), Pipeline (kanban across phases), current-year list with revenue forecast, previous year (unfinished items), All grouped by year.
- **CRM statuses**: Call (they contacted me, call to schedule) → Quote (after the call we see a fit; proposal sent) → Awaiting reply → Client → Lost; plus **Past clients** (worth recontacting in quiet periods).
- **CRM properties**: status, contact (email / Instagram — but move conversations to email), industry, website, request (updated through the stages), a dated timeline of steps (call, no reply, follow-up…), to-do (e.g. "waiting for material"), forecast revenue, linked projects, linked invoices, created time.
- **Contacts** (potential collaborators): profession (multi-select tag), email, phone, portfolio/Instagram link.
- **Notes**: tags such as travel, personal project, first contacts, outlines, scripts; date added; linked project (presentation scripts, client meetings).
- **Invoices**: number; issue date (also issued in the accountant's portal, but mirrored for overview); **cash-in date**; Year computed from cash-in; client (relation); linked projects; status (To issue/send — rarely needed if projects use "To invoice" — To collect, Paid); automatic amount (rollup of linked projects' amounts, summing several projects on one invoice) **plus** a manual amount (stamp duty, deposits); notes.
- **Content** (one database for all channels — Instagram, TikTok, LinkedIn and a long-form channel): views Calendar (drag ideas onto dates), per-platform views, Ideas grouped by recurring series/rubric, **Pipeline** (To write → To design → To record → To edit), long-form list; properties: platform/social (relation to one page per network, for icons), type (e.g. vertical clip, carousel), series, tags, status, created date, Sponsored (checkbox).
- Content area also holds semester goals (follower targets — "nice to look at, not very useful") and a **personal-branding document** with your targets and *why/for whom* you create content.
- Personal area: expense tracker (daily entry, categories such as car, shopping, restaurants; weekly/monthly/yearly archives — categories are the most useful part), habit tracker (date, checkboxes, a progress ring), saved quotes.

Hour tracker (exact build):
- Database **Tracker**: Task (title), Start (Date with time, day/month/year, 24 h), End (duplicate of Start), Time (Formula), Project (Relation → Projects, **limit 1**, shown on Projects as "Tracker").
- Time formula: `dateBetween(prop("End"), prop("Start"), "minutes") / 60`. Do **not** use `"hours"`: Notion rounds, so 16:00–16:30 would show 1 instead of 0.5.
- Filter views by **End** date, not Start (filtering by Start makes rows vanish unexpectedly when dates differ): Today = End is this day; Week = End is this week; add a **Yesterday** view because hours are often logged the next day.
- In Projects: Total hours (Number, e.g. 14, 10, 5); Hours done = Rollup → Tracker → Time → **Sum**; Hours remaining = `prop("Total hours") - prop("Hours done")`; Hours % = `round(prop("Hours done") / prop("Total hours") * 100) / 100`, displayed as **Percent** with a coloured **bar**. Over 100% = budget overrun.
- Show the Tracker relation on the project page "as page section" with Start, End, Time visible, so you can add an activity from inside the project and it is linked automatically.
- Tracking is an approximate guide, not an obligation; its value is realistic timelines for clients and control of hour packages (e.g. 10 h on consumption).

Dashboard cosmetics: cover image; icons as emoji, Notion icons (recolourable) or your own (quickly drawn in a design tool); one approach colours client icons in the client's logo colours for instant recognition.

## Procedures
**Build the 3-database starter**
1. Create an empty page "Dashboard"; type "/" to add pages Projects, Clients, Notes, each with a new empty table database (not linked to an existing one).
2. Projects → rename the default view "Overview"; add Client (Relation → Clients, limit 1, show on Clients), Status, Dates (day/month/year, 24 h), Budget (Number, €; footer Sum); footer Count on Name.
3. Add view "Status": Board, group by Status, colour columns, show client and status.
4. Add view "Gantt": Timeline by date, show table with name + client, show status; zoom Quarter.
5. Add view "Revenue": table, filter Status = Done (or active + done), show only client and budget.
6. Clients: add Contact (Email), Status; the Projects relation appears automatically.
7. Notes: add Date (Created time), Project (Relation → Projects, show on Projects as "Notes"); sort Date descending.
8. In a project page add a **Linked view of database** → Notes, filter Project = this project. New notes created there are pre-linked — open it during calls with the client contact.
9. Set dashboard icons; check every view after adding relations (new columns may appear).

**Add the hour tracker**
1. "/" → full-page database "Tracker"; rename first view "Today".
2. Add Start, End, Time formula, Project relation as above.
3. Filter Today by End = this day; duplicate as Week (this week) and Yesterday.
4. In Projects add a "Tracker" view with Total hours, Hours done (rollup sum), Hours remaining, Hours % (percent bar), hiding everything else.
5. Test: 8:00–10:00 → 2; 14:00–14:30 → 0.5; log 3 h on a 10 h project → 7 remaining, 30%.

**Learn before building**
1. Browse free and paid templates on Notion's site, also outside your category, and inspect their databases, properties, filters.
2. Study others' systems for the reasoning, then start from zero, keeping only what you need.
3. Sketch the four answers on paper or tablet notes.

**Monthly maintenance**
1. Archive Done projects into the yearly group; move silent leads to Lost or Past clients.
2. Check invoices in To collect; update cash-in dates.
3. Remove properties nobody fills (e.g. a forgotten Quote field) or make them part of onboarding.
4. Review the Energy mix of active projects before accepting new ones.
5. Add new Notion features only when they answer an existing question.

## Common Mistakes
- Opening Notion with no requirements → answer the four questions on paper first.
- Duplicating a template or copying someone's workspace → rebuild from zero, using it as reference.
- One database per project type → one Projects database with generic properties.
- A table for date-driven questions → Timeline/Gantt.
- Views showing every property → show only what the view's goal needs.
- Revenue total including deleted or never-started projects → filter by status.
- `dateBetween(..., "hours")` → minutes / 60.
- Filtering tracker views by Start → filter by End.
- Invoices grouped by issue year under a cash-basis regime → compute Year from the cash-in date.
- Expecting the workspace to be final → schedule periodic pruning; it keeps evolving.

## Mental Models
- Views are questions: "what is active?" (board), "when am I free?" (timeline), "how much will I earn this year?" (filtered table with sum), "what did I do today?" (filtered tracker).
- A rollup is the bridge that turns raw logs into decisions: hours logged anywhere become a project's progress bar.
- Notion works brilliantly for one person; team use was never tested in this system, so validate before rolling it out to a team.
- Notion is "difficult only if you don't know what you need" — after that it "creates addiction".
- Tool hopping is research: spreadsheets became unmanageable (too many sheets, fragile formulas), Airtable's free plan felt limiting, task-only apps (Todoist) don't manage projects well; each failure clarified the real needs.
- Projects are the hub; everything else (clients, notes, hours, invoices) hangs off them.
- The Gantt is a sales tool: it tells you when you can honestly promise a start date.
- The Energy field captures what hours don't: two overlapping light projects are fine, two heavy ones are not.

## Examples
- A sample space with Project 1–3, Client 1–3, Note 1–4: moving Project 2 from Client 1 to Client 2 instantly updates both client pages; Note 4 created inside Project 1's linked view is auto-linked.
- Before a call with a new client, the Quarter Gantt shows four deliveries in the next month, so the designer proposes starting in a month.
- A 10-hour package project: three logged sessions show 50% used; at 110% the bar signals the overrun before invoicing.
- A December invoice paid in January appears under next year's income because Year is computed from cash-in.
- A content idea from a follower's DM ("how do I apply a palette I found online?") is logged as an idea, typed as vertical clip, assigned to a series, then moved through write → design → record → edit.
