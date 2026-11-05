---
name: events
title: Events and associations (playbook)
description: |
  Entry point for trade shows, conferences, regional and trade association meetings,
  speaking slots, hosted dinners and webinars: "should we do this show", "what do we
  need for", "where are we at with the conference", "booth", "attendee list", "lead
  capture", "follow up from the show", "the association meeting", "speaking deadline".
  Routes the plays by phase: decide, plan, outreach, prep, capture, follow up, debrief.
collection: events
type: playbook
reads: [5-current/calendar.md, 1-context/ideal-customer.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [event-scorecard, event-plan, event-outreach, event-prep-deck, event-lead-ingest, event-follow-up, event-debrief, association-play, speaking-proposal, webinar-play]
playbook: 14
stage: distribution
---

This applies to every event. It produces the right play for where the event is in its life, and holds the rule that a show is a pipeline event, not an awareness channel.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the events system of record named in `1-context/stack.md`. Find the event's row: owner, dates, decision, status.
2. Route by phase:
   - Not yet decided → `event-scorecard`.
   - Decided, more than the minimum lead time out → `event-plan`.
   - Inside eight weeks → `event-outreach` (lists, meetings, booth draw), then `event-prep-deck`.
   - Show days → `event-lead-ingest` daily.
   - After the show → `event-follow-up` by tier, then `event-debrief` at the horizon.
   - An association rather than a show → `association-play`.
   - A speaking opportunity → `speaking-proposal`.
   - A hosted dinner or webinar → `webinar-play`.
3. On every request, check the three things that fail most often: is there an attendee or member list and when does it arrive; who owns lead capture on site and how do scans reach the CRM; who owns follow-up and by when.
4. Report status as a table: done, pending, overdue, with owners, from the system of record. Keep open decisions in their own section.

## KPIs (per show)

- Pre-show meetings booked.
- MQLs and SQLs by tier; demos on site and booked after.
- Existing customers met; closed-lost re-engaged.
- Closed won ARR at the payback horizon; cost per qualified lead all in.
- Team debrief score.

## What good looks like

- The best operator spends most of the effort before and after the show. Ninety percent of the value is in the list work, the booked meetings and the follow-up; the booth is where it gets converted.
- The mediocre version is a great booth and a pile of scans nobody worked. The tell is "let's talk when we're back".
- Good output is a show where every scan was tiered the same day, every hot lead was contacted within the SLA, and the debrief can state ARR at the horizon.

## Rules

- MUST say no to a show inside the minimum lead time in `5-current/calendar.md`.
- MUST keep logistics in the events system of record, not in chat or a deck.
- NEVER treat a show as a cold-awareness channel, a substitute for outbound, or a venue for internal events.
- NEVER buy attendee lists.
