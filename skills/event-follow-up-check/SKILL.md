---
name: event-follow-up-check
title: Event follow-up check
description: |
  Run this loop daily through the follow-up window after any event: "where are we on the event
  leads", "did everyone get followed up", "the post-event check". Reads the event's
  lead list and the CRM, finds every lead past its SLA window with no touch, and
  produces the list by owner with the draft to send, plus the running count toward
  the event's scorecard target.
collection: events
type: loop
cadence: daily, through the follow-up window after an event
reads: [3-strategy/funnel.md, 5-current/calendar.md, 1-context/stack.md]
related: [event-follow-up, event-lead-ingest, event-debrief, event-scorecard, demo-routing, weekly-channel-update]
playbook: 14
stage: distribution
---

This runs every morning from the day after the event until the debrief. It produces the list of leads that are about to go cold and the number the debrief will judge the event on.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The loop

1. Load `gtm-context` and `5-current/calendar.md`; find the event in its follow-up window and its scorecard target from `event-scorecard`.
2. Pull the event's leads from the CRM via the tag `event-lead-ingest` applied. For each: tier, SLA window (Hot, Warm, Cold from the follow-up SLA in `5-current/calendar.md`), last touch, owner, status.
3. Find every lead past its window with no logged touch, and every lead whose next step is due today. Group by owner.
4. For each, pull the draft from `event-follow-up` if one exists, or generate it with the booth note and the leave-behind link. The owner sends.
5. Count toward the target: leads, follow-ups sent, replies, demos booked, demos held. Compare to the plan's day-by-day expectation.
6. Deliver the list to each owner and the count to the marketing lead. Flag an owner with more than a day's backlog.
7. On the last day of the follow-up window set in `5-current/calendar.md`, hand the final counts to `event-debrief`.

## What good looks like

- The best operator makes the first week after the event the busiest week of the quarter for sales.
- The mediocre version sends one blast a few days later and reports scans as leads.
- Good output is zero Hot leads past their SLA without a touch, and a debrief with real demo numbers.

## Rules

- MUST use the follow-up SLA windows from `5-current/calendar.md`.
- MUST count demos booked and held, not scans, toward the target.
- NEVER send a follow-up; the owner sends.
- NEVER stop before the follow-up window ends unless the debrief is done.
