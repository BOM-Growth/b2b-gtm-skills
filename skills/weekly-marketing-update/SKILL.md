---
name: weekly-marketing-update
title: Weekly marketing update
description: |
  Use this skill every week: "the weekly update", "marketing numbers for the leadership
  meeting", "what did marketing do this week", "the Monday report", "MQLs this week".
  Produces one page: the funnel counts by source against last week and the quarter's
  pace, spend by channel, the three things that happened, the three things next week,
  and the open decisions.
collection: measurement-and-reporting
type: play
reads: [3-strategy/funnel.md, 1-context/stack.md, 5-current/calendar.md]
related: [reporting-experiments, funnel-definitions, paid-weekly-report, experiment-readout, decision-log, weekly-channel-update]
playbook: 15
stage: operate
---

This applies weekly, same day, same shape. It produces the page leadership reads in two minutes and the record the quarterly plan is built from.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the week's counts from the CRM on the stage definitions there: leads, qualified, demo requests, demos held, opportunities, by first-touch source. Never from a platform dashboard.
2. Pull spend by channel from `paid-weekly-report`. Pull reach numbers for coverage channels as coverage, not as conversions.
3. Lay the table: this week, last week, four-week average, quarter to date against the quarter's target pace. One row per source; a source with corrected attribution carries its caveat from `lead-source-audit`.
4. Three things that happened: shipped, learned, broke. Each in one line with a number.
5. Three things next week: with the owner and the number that will say it worked.
6. Open decisions for leadership, each with the recommendation and the cost of waiting. Log any decision taken in `decision-log`.
7. Add the event or launch line when `5-current/calendar.md` has one in the next thirty days: status against the plan, leads so far.
8. Keep the page the same shape every week. Deliver as a doc or a message the human posts; never post automatically.

## What good looks like

- The best operator reports the same numbers every week and explains every swing in one line.
- The mediocre version changes the metrics each week to the ones that look good.
- Good output is a page where a reader who missed a month can tell what changed from the table alone.

## Rules

- MUST count from the CRM on the `3-strategy/funnel.md` definitions.
- MUST keep the table's shape across weeks.
- NEVER mix platform conversions with CRM counts.
- NEVER post or send; the human does.
