---
name: event-plan
title: Event plan
description: |
  Use this skill once a show is a go and it is more than the minimum lead time out: "plan
  the show", "what do we need for", "where are we at with", "the checklist", "booth
  logistics", "who's going", "travel", "sponsorship deliverables". Produces the dated
  checklist in the events system of record from lead time to the post-show horizon, with
  owners and status, and a status table on request.
collection: events
type: play
reads: [5-current/calendar.md, 1-context/stack.md, 2-standards/proof-rules.md]
related: [events, event-scorecard, event-outreach, event-prep-deck, event-lead-ingest]
playbook: 14
stage: distribution
---

This applies from the decision to the debrief. It produces one dated plan in the system of record and a status view anyone can read.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the events system of record named in `1-context/stack.md`. Create or open the event's row: dates, location, booth, sponsorship, owner.
2. Name the event owner (on site, arrives early) and the roles: who staffs the booth, who runs demos, who books and takes meetings, who captures leads, who follows up.
3. Lay the checklist on phases counted back from the show: decision, early planning, outreach, final prep, show days, the days right after, post-event, and the payback horizon. Take the phase start dates from `5-current/calendar.md` (minimum lead time, outreach window, final prep, follow-up window, payback horizon); ask the person for any that are missing. Each item has an owner and a date. The full checklist lives in the system of record, not in this skill.
4. Set the fixed decisions by phase: speaking application as soon as the show is a go; booth draw decided and team gear ordered by the dates in `5-current/calendar.md`; attendee list request and pre-show comms at the start of outreach; prep deck and talk-track drill in final prep; lead scanners counted against booth size.
5. Confirm lead capture before anything else: scanners or a form that maps to CRM fields, who initials each scan, how scans reach the CRM the same day.
6. Confirm the attendee or member list and its arrival date. If the organizer gives none, source exhibitor, member and past-attendee company lists and ask who is going.
7. Record everyone's arrival and departure times in the system of record, so opening and closing coverage can be checked.
8. On request, return a status table: item, status (done, pending, overdue), owner, date, notes. Open decisions in their own section.

## What good looks like

- The best operator locks lead capture and the list first, because those are the two things that fail most and cannot be fixed on site.
- The mediocre version plans the booth beautifully and finds out the week before that the attendee list arrives after the show.
- Good output is a plan where the overdue column is empty by final prep and the on-site team knows its shifts before it travels.

## Rules

- MUST keep the plan in the events system of record; chat and decks are not the record.
- MUST confirm lead capture and list arrival before outreach starts.
- NEVER leave arrival and departure times out of the record.
- NEVER let an item exist without an owner and a date.
