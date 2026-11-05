---
name: monthly-experiment-readout
title: Monthly experiment readout
description: |
  Run this loop on the first working day of the month: "the monthly readout", "what
  did we learn last month", "scale or kill review", "the bets review". Collects every
  experiment verdict from the month, the channel reads that are monthly by nature
  (paid social, search visibility, AI answer visibility, content), and produces the
  one page of verdicts, lessons and the budget moves they imply.
collection: measurement-and-reporting
type: loop
cadence: monthly
reads: [3-strategy/funnel.md, 5-current/calendar.md, 1-context/stack.md]
related: [experiment-readout, experiment-brief, decision-log, linkedin-ads, aeo-review, seo-audit, content-calendar, quarterly-gtm-plan]
playbook: 15
stage: operate
---

This runs monthly. It produces the page the quarterly plan is built from three times a quarter, so the plan is a summary of verdicts rather than a fresh argument.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The loop

1. Read the context (see Before you start). Pull every experiment in `decision-log` with a readout in the month; confirm each has a verdict from `experiment-readout`. A missing verdict is run now or logged as missed with the reason.
2. Run the monthly channel reads: `linkedin-ads` (reach into the TAM, engaged accounts), `aeo-review` (prompt presence trend), the `seo-audit` keyword set, the `content-calendar` output against plan.
3. Collect the month's weekly tables from the reporting history; compute the month against the quarter's pace.
4. Write the page: verdicts (scale, kill, extend) with the one number each; the channel reads with the trend; the lessons in one line each; the budget moves implied, typed cut, scale, build, test.
5. Propose next month's briefs through `experiment-brief` for anything the lessons suggest; three to five at most.
6. Log the decisions requested in `decision-log`. Deliver the page for the human to share.

## What good looks like

- The best operator ends each month with a short list of kills and one scale, and the budget already moved.
- The mediocre version reviews experiments at the quarter's end from memory.
- Good output is a page the quarterly plan can paste its evidence section from.

## Rules

- MUST have a verdict or a logged miss for every experiment due.
- MUST type every budget move cut, scale, build or test.
- NEVER let an experiment run into a second month without a verdict or an extension entry.
- NEVER share the page automatically; the human shares.
