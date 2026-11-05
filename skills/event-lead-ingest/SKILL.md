---
name: event-lead-ingest
title: Event lead ingest
description: |
  Use this skill on every show day and the day after: "process today's scans", "tier the
  leads", "who did we meet", "get the badge scans into the CRM", "end of day summary",
  "the scans are a mess". Produces every scan in the CRM with the event as source, a tier
  (hot, warm, cold) with its follow-up deadline, the stage (MQL, SQL, SAL), the scanner's
  notes, and the end-of-day summary to sales.
collection: events
type: play
reads: [3-strategy/funnel.md, 1-context/ideal-customer.md, 5-current/calendar.md, 1-context/stack.md]
related: [events, event-follow-up, audience-icp-filter, inbound-triage]
playbook: 14
stage: distribution
---

This applies the same day a lead is captured. It produces leads sales can act on before the team flies home.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the follow-up SLA in `5-current/calendar.md`.
2. Pull the day's captures: scanner export, the backup form, photographed badges. Every capture carries the scanner's initials, the person's role, what they asked, and the next step. A scan with no note goes back to the scanner before the huddle ends.
3. Run `audience-icp-filter` on the day's rows. Internal, vendors, media and competitors go to the stripped sheet.
4. Set the stage: every scan is an MQL; flag SQL where the scanner starred it or the gates pass; mark SAL where a demo was shown or a time was booked on site.
5. Set the tier and deadline: hot (demo booked or asked for a call) within 24 hours; warm (qualified, interested) within 48 hours; cold (ICP but no signal) into nurture within a week. Defaults from `5-current/calendar.md`.
6. Write to the CRM: contact, company, source = the event name, stage, tier, deadline, notes, owner. Create the deal at the first pipeline stage where a demo is booked.
7. Send the end-of-day summary to sales: counts by tier and stage, the hot list with notes, the customers met, the product feedback worth passing to product (quality over quantity, with how strongly it was felt).
8. On the last day, reconcile the full list against the booked-meeting list from `event-outreach` so no pre-booked meeting is lost.

## What good looks like

- The best operator insists on notes at the moment of scanning. A scan without a note is a name, not a lead, and it will not be followed up.
- The mediocre version exports the scanner at the end of the show, uploads it a week later, and the hot leads have gone cold.
- Good output is a CRM view on the last show day where every scan has a tier, a deadline and an owner, and sales has already started on the hot ones.

## Rules

- MUST process every day's scans the same day.
- MUST set the event name as the lead source on every record.
- NEVER drop a scan; out-of-ICP goes to the stripped or cold sheet with a reason.
- NEVER create a deal without a booked demo or an on-site demo held.
