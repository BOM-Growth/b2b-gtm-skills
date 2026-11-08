---
name: experiment-brief
title: Experiment brief
description: |
  Use this skill before any test starts: "let's try", "should we test", "an experiment
  on", "run a pilot of", "I want to see if", "a bet on". Produces the brief: the
  hypothesis, the one metric and its threshold, the budget and time box, the kill
  criteria, the owner, the readout date, and the decision it informs, logged before
  the first dollar.
collection: measurement-and-reporting
type: play
reads: [3-strategy/funnel.md, 5-current/calendar.md, 2-standards/proof-rules.md]
related: [reporting-experiments, experiment-readout, decision-log, event-scorecard, quarterly-gtm-plan]
playbook: 15
stage: operate
---

This applies before every bet, large or small. It produces the brief that makes the readout honest, because the success number was written down before the test ran.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Write the hypothesis in one sentence: if we do X for audience Y, metric Z moves to threshold T within time U.
2. Pick the one metric from `3-strategy/funnel.md` the test is judged on. A test that will be judged on three metrics is three tests or none.
3. Set the threshold and the time box before the budget: the number that means scale, the number that means kill, the date of the readout. Default to the shortest window that can show the signal.
4. Set the budget and the kill criteria: the spend or time at which the test stops early if the leading indicator has not moved.
5. Name the owner, the decision this test informs (what gets more budget, what gets cut), and who makes it.
6. Check `5-current/calendar.md` for conflicts: a test that straddles a launch, an event or a slow season will not read cleanly.
7. Log the brief in `decision-log` with the readout date. Schedule the readout through `experiment-readout`.

Use `references/brief-template.md` for the form.

## What good looks like

- The best operator writes the kill number first and the budget second.
- The mediocre version launches the test and decides what success means when the numbers come in.
- Good output is a brief a stranger could grade without asking the owner anything.

## Rules

- MUST state one metric, one threshold and one readout date before the test starts.
- MUST log the brief in `decision-log` before any spend.
- NEVER change the threshold after the test starts; log a new brief instead.
- NEVER run a test with no kill criteria.
