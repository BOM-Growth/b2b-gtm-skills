---
name: demo-routing
title: Demo routing
description: |
  Use this skill when a fit lead needs a rep and a slot: "route this demo", "who owns
  this account", "the demo didn't get booked", "the handoff to sales", "round robin",
  "the rep brief for tomorrow's demo". Produces the owner assignment with the reason,
  the booking path, the rep brief (account, persona, source, what they asked for), and
  the handoff log.
collection: crm-and-tracking
type: play
reads: [3-strategy/funnel.md, 1-context/ideal-customer.md, 1-context/personas.md, 1-context/stack.md]
related: [inbound-lifecycle, inbound-triage, lead-source-audit, event-lead-ingest, signal-to-outreach]
playbook: 8
stage: build
---

This applies whenever a lead is routed. It produces a booked demo with a rep who walks in prepared.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Take the lead from `inbound-triage` with its tier, intent and source.
2. Assign the owner by the rules in `3-strategy/funnel.md`: existing account to its owner, territory or segment where defined, otherwise the rotation. Record the reason on the record.
3. Booking: the lead gets the owner's booking link or a proposed time within the SLA; if the lead already booked through the site, confirm the slot landed on the right rep's calendar.
4. Write the rep brief in six lines: company and tier, person and persona, source and what they consumed, what they asked for, any history in the CRM, the one question to open with.
5. Log the handoff: time routed, owner, slot, brief sent. The clock stops at the booked demo, not at the assignment.
6. Watch the misses: a demo request not booked within the SLA goes back to the triage queue with a flag; a no-show gets one reschedule draft and a note.
7. Report weekly in `weekly-marketing-update`: requests, booked, held, by source; the gap between request and held is the number sales and marketing both own.

## What good looks like

- The best operator measures request to held, not request to assigned.
- The mediocre version assigns the lead and considers it handed off.
- Good output is a rep who opens the demo knowing what the lead read and why they asked.

## Rules

- MUST record the assignment reason on the record.
- MUST send the rep brief before the demo.
- NEVER let a demo request pass the SLA without a flag back to triage.
- NEVER book on the lead's behalf without the rep confirming the slot.
