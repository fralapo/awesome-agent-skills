# Chapter 38: Onboarding, Permissions, Paywall and Cancellation Flows

## Core Idea
Onboarding is the second gate after someone decides to install: if people do not finish it, nothing behind it matters. Its job is threefold: build trust, move people through with the least friction, and set expectations about what happens inside. The same logic extends to the two other commitment moments, the paywall and the cancellation screen. ch20 supplies the psychology (goal gradient, peak-end); ch34 the structural audit; ch32 transactional flows; this chapter is the flow design.

## Three Ways Onboarding Fails
1. **Asking too much before giving value**: long forms and permission requests up front. A seven-step sign-up that collects data and then never uses it also teaches users the data is pointless.
2. **Not setting expectations**: users do not know how many steps remain, what comes next or what the product will do with their answers.
3. **Feeling generic**: nothing in the flow reflects who the user is or why they came.
There is also a fourth, opposite case: no onboarding at all. If the creator needs an hour to explain a simple app, a new user is lost. If the product has no value until set-up is done, put the set-up inside onboarding.

## Flow Rules
- **Native, not a web view** of the website inside the app. Sign-up and login are native screens.
- **No duplicate screens**: a splash and a login that say the same thing merge; a welcome screen can double as sign-up and login.
- **Offer Apple/Google sign-in** as the fast path.
- **Role choice gets its own page** (buy vs sell, learner vs teacher), so each path can be explained and tailored.
- **Typical length**: about four to five screens, e.g. welcome, create account, location explanation, notifications explanation, then the app. Everything else can wait until it is needed (progressive disclosure, ch19).
- **Show progress** ("step 2 of 5", "3 minutes left"), not a bare task (goal gradient, ch20). A progress bar tends to raise completion.
- **Show the product's value early**: a demo on the first screen, or the first action already delivers the core outcome (log a meal with a photo; a note-taking tool produces the notes at the end of the first call). The time to this **aha moment** is the metric to shrink.
- **Use the answers**: ask goal and available time, then tailor a plan or content. Collect only what you use in the next ten minutes.
- **Include the real onboarding copy and screen order in any brief** (design, PRD or AI prompt); the copy shapes the layout.
- **Attribution step**: one cheap question, "Where did you find us?", gives acquisition data from day one. Add it before launch, not in week three, because most downloads arrive in the first weeks (ch41).

## Emotional Arc for Onboarding Copy
Introduce the product, learn who the user is, show the problem and what it costs over time, show how the product resolves it, show the outcome. Each screen moves one step along this arc, and the user's earlier answers appear in later screens.

## Permission Prompts
- Never fire the system dialog cold. Show a **pre-permission screen** first: what the app does with the permission and what the user gets from it ("Allow location to see pickup points within 2 km").
- Reason: the operating system lets the app ask once; after a denial it can only point to settings. A pre-permission screen lets the user decline without burning the real prompt.
- Ask at the moment of need when possible (location when the map opens). Notifications: explain which messages and how often.

## Empty States as Part of Onboarding
After onboarding the user lands on a screen with no data. Fill it with the next step: "Start browsing", people to follow, upcoming events, "Create your first X". A bland empty state wastes the aha moment onboarding just prepared.

## Paywall Models
- **Hard paywall after onboarding** (trial, then an annual plan) suits low-ticket apps and apps with running costs (AI calls, storage, content licensing). The user has already invested time answering questions (sunk effort), and the first revenue funds growth tests.
- **Freemium** suits higher-ticket products or ones with a real free scope. Free tiers attract many non-paying users, blur the product-market-fit signal and convert a small share.
- Paying users give better signal, feedback and word of mouth than a larger free base. Pick the model by price point and running cost, and decide before building.
- **Paywall screen**: show only what differs between tiers; keep benefit lists short; state price, billing period and trial end date plainly; show how to cancel (ch34 tiers). Preview the value the user just experienced rather than abstract features.
- Test the paywall on a real device: an existing subscription on the test account skips the real trigger, and time-based triggers cannot be tested by clicking through.

## Cancellation Flows
- Make cancellation **short and transparent**: one clear path from the account area, exact end date, what is lost, any penalty or refund rule.
- A ten-step cancel flow may retain some users but erodes trust, generates negative reviews and complaints, and in many jurisdictions breaches consumer rules (cancelling should be about as easy as subscribing).
- One honest retention step is fine: a short reason question, an offer to pause or downgrade, a reminder of what will be lost. Then a visible "Confirm cancellation" button. No fake confirm buttons, no guilt-trip wording, no hidden links.
- Send a confirmation with the end date; send a reminder before a trial converts to paid.
- Treat the cancellation reason as research data: tally it and feed it to the roadmap (ch10).

## Procedure: Onboarding Audit and Refresh
1. State the onboarding goal: trust, low friction, expectations.
2. Walk the flow on a clean install; time it and count screens and fields.
3. Mark each step as needed now / needed later / unused; cut or defer the last two.
4. Merge duplicate screens; check native sign-in options.
5. Add progress, the pre-permission screens and the attribution question.
6. Check the first action delivers value; measure time to aha.
7. Review empty states and the paywall/cancel pair as one commitment chain.
8. Measure completion per step and the funnel to the paywall (ch10); iterate on the biggest drop-off.

## Mistakes
- Asking for permissions at launch with no explanation.
- A web view for sign-up; duplicate welcome and login screens.
- Collecting data without using it; no way to see progress.
- A paywall before any value is shown; unclear trial end date.
- A cancel flow that is harder than sign-up.
- Optimising onboarding visuals before checking where people actually drop off.

## Checklist
- [ ] Goal named; screens counted; every step justified.
- [ ] Native sign-up, Apple/Google sign-in, no duplicates.
- [ ] Progress visible; aha reached quickly.
- [ ] Pre-permission screens for location and notifications.
- [ ] Attribution question present.
- [ ] Empty states point to a first action.
- [ ] Paywall model matches price and running cost; terms plain.
- [ ] Cancellation short, honest, confirmed by message.

## Connects To
ch10 (measuring), ch16 (flows), ch19 (progressive disclosure), ch20 (goal gradient, peak-end), ch32 (transactions), ch34 (tiers and paywall cards), ch37 (trust levers), ch39 (retention), ch41 (what to polish first).
