---
name: event-follow-up
title: Event follow-up
description: |
  Use this skill from the day after a show until every lead has an outcome: "follow up
  from the show", "where are the event leads", "has anyone contacted them", "is follow-up
  happening", "what happened to the scans". Produces the sequence per tier, the
  owner and deadline per lead, and a view of every event lead with its action, meeting
  and outcome, so the leak is visible.
collection: events
type: play
reads: [3-strategy/funnel.md, 5-current/calendar.md, 2-standards/brand-voice.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [events, event-lead-ingest, outbound-sequence-copy, reply-handling, nurture-email, event-debrief]
playbook: 14
stage: distribution
---

This applies after the show. It produces the part of the event most teams skip, and the number the debrief depends on.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the SLA in `5-current/calendar.md`. Pull every lead with the event as source from the CRM, with tier, deadline, owner and current status.
2. Hot leads: the owner contacts them inside the hot SLA with the specific next step from the scan notes (the file they said they would send, the time they wanted). No template for hot leads; the note is the message.
3. Warm leads: a three-touch sequence inside the warm SLA through `outbound-sequence-copy`, anchored on what was shown at the show (the draw, the customer who was there) and one ask: book a time.
4. Cold leads: into `nurture-email` inside the cold SLA with the event tagged, so the next send mentions it.
5. Build the follow-up view: every event lead, tier, owner, first action date, meeting booked, outcome. Review it in the daily or weekly pipeline huddle until every row has an action.
6. Escalate rows past their deadline with no action to the sales lead by name. Do not reassign silently.
7. Feed meetings and deals created from the event back to the CRM with the event source intact, so `event-debrief` can count them at the horizon.

## What good looks like

- The best operator treats the follow-up view as the real event deliverable and keeps it in front of the sales lead until it is empty.
- The mediocre version sends one "great to meet you" email to everyone and files the scans.
- Good output is a view where every hot lead was contacted inside the SLA with the thing they asked for, and the meetings column is filling soon after the show.

## Rules

- MUST contact every hot lead within the SLA using the scan notes.
- MUST keep the event as the source on every meeting and deal it produces.
- NEVER send a generic thank-you as the only follow-up to a hot or warm lead.
- NEVER let a lead past its deadline sit without a named escalation.
