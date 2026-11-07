# Chapter 34: Interface Audit and Redesign Method

## Core Idea
Before changing visuals, diagnose. Most weak interfaces fail on the same things: the main task is buried, the same destination is reachable several ways, navigation repeats home content, and nothing says which element matters most. A redesign reorganises first and restyles second. This chapter is the audit order and the structural fixes; ch17 lists beginner visual mistakes, ch18 the visual fundamentals, ch32 transactional flows.

## Pick the Goal of the Redesign
A redesign serves one of three goals, and mixing them blurs decisions:
- **Design**: modernise the look.
- **Strategy**: promote a feature, offer or purchase.
- **Usability**: fewer, simpler steps.
If the product already works well, the work is refinement, not reinvention. Do light user and market research first and apply the brand guidelines inside the interface rather than leaving them in a separate document.

## Audit Order (per screen)
1. **Purpose**: what is the one goal of this page or screen? One page per user goal.
2. **Hierarchy**: are controls ranked by importance and frequency? One primary action per view.
3. **Consistency**: one component set, one text scale, one corner-radius style, one button size per action.
4. **Navigation**: one path per action; no duplicates.
5. **Colour**: does each colour carry meaning? (ch35)
6. **Layout**: group related items, order by priority, check reach.
7. **Platform guidelines**: names, patterns and gestures the platform users already know.

## Structural Fixes
- **Merge duplicates**: two pages with the same goal become one. A page that only repeats home content (or a second "home") is deleted and its useful content moved to where it is used. A card that opens a page and a "details" button that opens the same page should not both exist.
- **Do not repeat the home in the menu**: a side panel or hamburger menu that mirrors home items adds nothing. A persistent panel navigates; it does not recommend what the homepage already recommends.
- **Profile-specific items go in the profile**: account, orders, history, downloads, privacy, notifications, benefits. Merge screens that show the same entity twice (profile and loyalty card).
- **Keep the bottom bar small**: three items let one carry more weight. Name it correctly (a tab bar, not "menu"). It should stay on sub-pages.
- **Overflow (three-dot) menus** hold secondary information at the end of the reading order, never core links or footer content hidden behind an ellipsis.
- **Search belongs where it is needed**: persistent on every page if it is a core action; in a small app, users should find, not search. Put the submit control next to the input or use Enter; a search field comes first, filters after.
- **Make the main task visible**: the most frequent job (top up, pay, check data) is a primary button, not a menu entry. Key functions hidden behind one switcher or in another app's sub-menu are a hierarchy problem; group by mode and expose the rest in a visible drawer.
- **Cut aggressively on dense screens**: the more actions offered, the fewer are read. Sequence: remove duplicates, demote rare items, group by intent, then reorder by frequency. Use a compact icon rail instead of a full sidebar when space allows.
- **Group content by intent** in horizontal carousels (quick, long-form, music). Keep "trending" separate from filters: it answers a different question. Carousels show one item at a time with pagination and a visible swipe affordance.
- **Cluster by proximity**: place a control next to what it acts on (delete beside the text, the close-keyboard arrow apart). Persistent actions stay visible on every page.
- **Reduce steps**: a three-screen purchase path becomes two where possible; an intermediate screen that only repeats the previous one is merged.
- **Surface needed data where it is used**: platform and seat on the ticket, not behind a lookup; a cross-sell only if the product is visible before it is added; delivery info beside the purchase action.
- **Tiers and paywall cards**: show only what differs between tiers, keep benefit lists short, do not repeat what all tiers include; in a selection flow choose by price first, then category.
- **Make promotions concrete**: "60% off to Rome" beats an abstract discount label. Label banners with what they are, and keep ad banners out of functional layouts.
- **Use real names for jargon**: explain in-product terms with clear labels; use well-known icons (a bell for notifications; a question mark reads as an error).
- **Social connection**: a long technical ID is poor UX; offer share, contact sync or a QR code. Progress, not just a count, makes gamification meaningful. A daily check-in that unlocks a reward is one engagement lever (ch20 ethics apply).
- **Modals near the trigger**: shorter pointer distance to the next target means faster action (Fitts's law). Keep scroll direction the same between similar lists.
- **Alternative modes must differ clearly**: a "theatre mode" that enlarges the player a little while the rest stays visible is not a mode. Keep a competitor's format separate from the main product instead of copying it in.
- **Learn from real flows**: study a pattern library before designing; copy structure, not visuals. Eye-scan logic: a single distinct item (colour, size, icon) interrupts scanning; use these stops sparingly.

## Procedure
1. State the redesign goal (design, strategy or usability).
2. List every screen with its one purpose; mark duplicates.
3. Rank actions by frequency; decide the one primary per view.
4. Cut and merge, then group and reorder.
5. Define the shared components, text scale and radii; apply.
6. Review against platform conventions and test the main task with five users (ch08).

## Mistakes
- Restyling before fixing structure.
- Making a button larger to nudge users instead of ranking it properly.
- A menu that repeats the home screen; two buttons to the same page.
- Same-weight buttons side by side.
- Decorative containers and ornaments that add nothing.
- Copying a visual language without checking legibility (ch35).

## Checklist
- [ ] Goal of the redesign named.
- [ ] Each screen has one purpose; duplicates merged.
- [ ] One primary action per view; ranking by frequency.
- [ ] Navigation: one path per action, small bottom bar, profile items in the profile.
- [ ] Data is shown where it is used.
- [ ] Reviewed against platform guidelines.

## Connects To
ch12 (iceberg), ch16 (flows), ch17, ch18, ch19, ch20, ch32 (kiosk and gesture), ch33 (consistency via components), ch35.
