---
name: quarterly-gtm-plan
title: Quarterly GTM plan
description: |
  Use this skill at the end of each quarter: "the plan for next quarter", "where should
  budget go", "what are we doing in Q", "the marketing plan", "the quarterly review".
  Produces the quarter's plan: the number by stage and by source, the budget by
  channel with cut, scale, build and test labels, the calendar of launches and events,
  the experiments, the owners, and the weekly pace the update will track against.
collection: measurement-and-reporting
type: play
reads: [3-strategy/funnel.md, 5-current/calendar.md, 1-context/ideal-customer.md, 1-context/stack.md]
related: [reporting-experiments, weekly-marketing-update, experiment-brief, decision-log, launch-calendar, event-scorecard, monthly-experiment-readout]
playbook: 15
stage: operate
---

This applies once a quarter, in the last two weeks of the prior one. It produces a plan the weekly update can measure, built from the quarter's verdicts rather than from ambition.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the quarter's history: the weekly updates, the experiment verdicts in `decision-log`, the event debriefs, the source table after `lead-source-audit`.
2. Read the funnel: conversion by stage and by source, over the quarter and the trailing year. Set the next quarter's number by stage from the sales target, backed into with the real conversion rates. Say where the gap is.
3. Classify every channel and program by the evidence: cut (no demo requests at any price), scale (demo requests at an acceptable cost with room), build (a lever the quarter will open), test (one experiment with a brief). Budget follows the labels.
4. Lay the calendar: launches through `launch-calendar`, events that passed `event-scorecard`, the dead zone, the content pillars. Nothing lands in the dead zone.
5. Pick the experiments: three to five, each with a brief through `experiment-brief` and a readout date inside the quarter.
6. Assign owners and the weekly pace per stage and source. The pace is what `weekly-marketing-update` reports against.
7. Write the one-page summary for leadership and the decision requests. Log the plan's decisions in `decision-log`.

## What good looks like

- The best operator sets the number from the conversion rates and then argues about which rate to move.
- The mediocre version sets the number from last year plus growth and allocates budget by habit.
- Good output is a plan where every dollar has a label and every label has evidence from the last quarter.

## Rules

- MUST derive the stage numbers from the sales target and real conversion rates.
- MUST label every channel cut, scale, build or test with the evidence.
- NEVER schedule a launch or a campaign into the dead zone in `5-current/calendar.md`.
- NEVER carry a channel forward without a verdict.
