---
name: weekly-channel-update
title: Weekly channel update
description: |
  Run this loop every week on the same day: "the Monday numbers", "run the weekly",
  "channel update". Chains paid-weekly-report, the funnel pull on the stage
  definitions, the experiment readouts due this week, and weekly-marketing-update into
  the one page leadership reads, then files the week's numbers so the month and the
  quarter are built from the same history.
collection: measurement-and-reporting
type: loop
cadence: weekly
reads: [3-strategy/funnel.md, 1-context/stack.md, 5-current/calendar.md]
related: [weekly-marketing-update, paid-weekly-report, experiment-readout, decision-log, lead-source-audit, monthly-experiment-readout]
playbook: 15
stage: operate
---

This runs weekly, same day, same order. It produces the weekly update and the history behind it without anyone rebuilding the table by hand.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The loop

1. Read the context (see Before you start).
2. Run `paid-weekly-report` for spend and cost per demo request by channel.
3. Pull the funnel counts from the CRM for the week on the stage definitions, by first-touch source. Apply the caveats from the last `lead-source-audit`.
4. Check `decision-log` for experiments with a readout date this week; run `experiment-readout` on each and collect the verdict lines.
5. Check `5-current/calendar.md` for launches and events in the next thirty days; collect the status line from the owner's plan.
6. Run `weekly-marketing-update` with all of the above. Deliver as a draft for the human to post.
7. File the week's table in the reporting history in `1-context/stack.md` so the monthly readout and the quarterly plan read from it.
8. Raise anything the table shows that needs a decision this week, with the recommendation, for `decision-log`.

## What good looks like

- The best operator runs this in the same hour every week and the update lands before the leadership meeting.
- The mediocre version pulls numbers when asked and the history has gaps.
- Good output is fifty-two tables a year in the same shape, and a quarterly plan built from them.

## Rules

- MUST run on the `3-strategy/funnel.md` definitions and from the CRM.
- MUST file the week's table in the history.
- NEVER post the update; the human posts.
- NEVER skip a readout that is due; a missed readout is logged as missed.
