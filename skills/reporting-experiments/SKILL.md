---
name: reporting-experiments
title: Reporting and experiments (playbook)
description: |
  Entry point for the operating rhythm: "the weekly update", "MQLs by channel", "what
  happened last week", "spend by channel", "experiment", "A/B test", "what are we
  testing", "readout", "quarterly plan", "board slides", "Q3 postmortem", "what are the
  rocks". Routes the weekly update, experiment briefs and readouts, and the quarterly plan,
  all on the shared funnel definitions.
collection: measurement-and-reporting
type: playbook
reads: [3-strategy/funnel.md, 1-context/stack.md, 5-current/calendar.md]
related: [weekly-marketing-update, experiment-brief, experiment-readout, quarterly-gtm-plan, funnel-definitions]
playbook: 15
stage: operate
---

This applies every week, every month and every quarter. It produces the numbers leadership sees, the decisions on live tests, and the plan the next quarter runs on.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Every number in this playbook uses those stage definitions and the systems of record in `1-context/stack.md`; if a number cannot be pulled from the system of record, say so rather than estimate.
2. Weekly, before the pipeline review: `weekly-marketing-update`. MQLs by channel, spend by channel, demos booked, and two lines on what changes next week. Events spoken to on their own line.
3. Any time a test is proposed: `experiment-brief`. One paragraph with hypothesis, metric, threshold, duration, owner, cost; ICE-scored into the backlog; three to five live at once; big swings, not button tweaks.
4. Monthly: `experiment-readout`. Each live test decided against its preset threshold and time box, logged, and the readout sent to the CEO.
5. Quarterly: `quarterly-gtm-plan`. Diagnostic first (what happened by channel and why), then two to three rocks with names, a done-well template per play, the activity calendar, and the content behind it. The plan feeds the board slides; it does not replace them.
6. Maintain `funnel-definitions` as the single reference; when a definition changes, log it and update every report the same week.

## KPIs

- Weekly update delivered before the pipeline review, every week.
- Experiments decided on time against their thresholds; share of decisions that were "scale".
- Quarterly plan agreed before the kickoff date in `5-current/calendar.md`.

## What good looks like

- The best operator reports leading indicators (MQL, SQL, demos) with the same discipline every week, so a dry month is visible in week two, not at quarter end.
- The mediocre version reports closed won in marketing's update, waits for statistical significance that never comes, and writes the quarterly plan from the solution backwards.
- Good output is a weekly table nobody argues with, a backlog where every test has a threshold, and a quarterly plan whose diagnostic a skeptic would accept.

## Rules

- MUST use the stage definitions in `3-strategy/funnel.md` for every number.
- MUST decide experiments on preset thresholds and time boxes, not on significance.
- NEVER report closed won as a marketing result.
- NEVER run more live experiments than the limit in `experiment-brief`.
