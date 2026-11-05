---
name: event-debrief
title: Event debrief
description: |
  Use this skill in the week after a show and again at the payback horizon: "debrief the
  show", "how did it go", "what did the conference produce", "was it worth it", "lessons
  for next year". Produces the KPI readout against the targets, the lessons by phase,
  the changes to the playbook, and at the horizon the payback verdict.
collection: events
type: play
reads: [5-current/calendar.md, 3-strategy/funnel.md, 1-context/stack.md]
related: [events, event-scorecard, event-lead-ingest, event-follow-up, decision-log]
playbook: 14
stage: distribution
---

This applies twice per show: the week after, for lessons, and at the horizon, for the verdict. It produces the record the next scorecard reads.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the targets set in `event-plan` and `event-scorecard`.
2. Week-after readout, from the CRM and the events system of record: pre-show meetings booked, scans, MQLs and SQLs by tier, demos on site and booked after, customers met, closed-lost re-engaged, product feedback captured, team debrief score from a short survey of the on-site team.
3. Lessons by phase: decision, planning, outreach, booth, capture, follow-up. One line each on what to keep and what to change. Ask the on-site team; do not write it from the plan.
4. Turn lessons into playbook changes: scanner count for the booth size, the draw that worked, the list source that arrived too late, the gear order date. Log each with `decision-log` and update `5-current/calendar.md` where a threshold moved.
5. At the horizon: closed won ARR with the event as source, fully loaded cost, cost per qualified lead, the payback verdict against the ratio in `5-current/calendar.md`.
6. Write the result to the event's page in the knowledge base (durable facts and results), leaving logistics in the system of record.
7. Decide next year: exhibit, attend, speak or pass, and the speaking deadline date.

## What good looks like

- The best operator writes the lessons while the team is still tired, and the verdict only at the horizon. Mixing the two produces optimism on week one and silence at month six.
- The mediocre version reports scans as results and never returns at the horizon.
- Good output is a page with two dates on it: the lessons, and the verdict with the ARR number.

## Rules

- MUST report against the targets set before the show, not against what was achieved.
- MUST return at the horizon and record the payback verdict.
- NEVER count scans or MQLs as the result; the result is SQLs, demos and ARR at the horizon.
- NEVER keep KPIs or deal values in the knowledge base; results stay in the system of record.
