---
name: experiment-readout
title: Experiment readout
description: |
  Use this skill when a test reaches its readout date: "did the test work", "readout
  on", "should we keep running", "the results of the pilot", "scale or kill". Produces
  the verdict against the brief's threshold (scale, kill, extend once), what was
  learned, the next brief if any, and the decision-log entry.
collection: measurement-and-reporting
type: play
reads: [3-strategy/funnel.md]
related: [reporting-experiments, experiment-brief, decision-log, weekly-marketing-update, monthly-experiment-readout]
playbook: 15
stage: operate
---

This applies on the readout date, not before and not later. It produces a verdict the brief already defined, so the result is a reading, not a debate.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the brief from `decision-log`. Take the metric, the thresholds and the time box as written.
2. Pull the metric from the CRM on the `3-strategy/funnel.md` definition for exactly the time box. Platform numbers are not the metric.
3. Compare to the thresholds: at or above scale, below kill, or between. Between gets one extension with a new readout date, never a second.
4. Write what was learned in three lines: about the audience, about the channel, about the offer. A kill with a clear lesson is a good result.
5. State the verdict and the action: scale (how much, from where), kill (what stops, what the budget goes to), extend (the new date and why).
6. Log the verdict in `decision-log` against the brief. Hand the line to `weekly-marketing-update` and the month's `monthly-experiment-readout`.
7. If the verdict is scale, write the next brief through `experiment-brief` for the scaled version; scaling is a new test.

## What good looks like

- The best operator reads the number against the brief and writes the verdict in a paragraph.
- The mediocre version finds a metric that moved and declares the test a success.
- Good output is a verdict the owner of the test would sign even when it is kill.

## Rules

- MUST judge on the metric and thresholds written in the brief.
- MUST log the verdict in `decision-log`.
- NEVER extend more than once.
- NEVER substitute a metric that moved for the one in the brief.
