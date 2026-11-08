---
name: outbound-cohort
title: Outbound cohort
description: |
  Use this skill at the start of each outbound week: "next cohort", "who do we go after
  this week", "cold, warm or closed lost", "bottom-up or top-down", "what's the angle
  for this group". Produces the cohort definition (who, why now, the angle, the persona
  ladder, the size), ranked against the other candidates, and the hand-off to list
  building and copy. See references/cohort-taxonomy.md.
collection: first-customers-and-outbound
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 3-strategy/funnel.md]
related: [outbound, build-target-list, outbound-sequence-copy, closed-lost-winback, signal-to-outreach]
playbook: 9
stage: distribution
---

This applies weekly. It produces one cohort with a reason to exist this week, so every send has an angle and every result teaches something.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Read the taxonomy in `references/cohort-taxonomy.md` and last week's results from `weekly-marketing-update`.
2. List candidate cohorts for the week: cold by segment and persona, warm (old prospects, past demos), closed-lost by reason, event follow-up, signal-driven, customer expansion. For each, the size and the angle in one line.
3. Rank by cheap to fail first. A small-account cold cohort tests a message at low cost; an executive cohort of named accounts goes last and gets call touches.
4. Set the persona ladder for the cohort: the practitioner first, then the manager a day later, then the executive with calls, per `1-context/personas.md`.
5. Define the angle as what changed or what they said: a new package for smaller accounts; a feature a lost prospect asked for; a customer near them they can meet. No angle, no cohort.
6. Set the size against the sequence owner's calendar and the plan for when the sales calendar fills up.
7. Hand to `build-target-list` for the names and `outbound-sequence-copy` for the words. Record the cohort, its angle and its send date so results can be read next week.

## What good looks like

- The best operator never sends the same message to two cohorts. The angle is the cohort.
- The mediocre version blasts a segment with the generic pitch and calls a 1% reply rate "outbound doesn't work for us".
- Good output is a one-paragraph cohort brief anyone can read next week beside its reply rate and say why it worked or not.

## Rules

- MUST give every cohort an angle tied to what changed or what the prospect said.
- MUST dedupe against active pipeline and the last 30 days of sends.
- NEVER run the whole TAM as one cohort.
- NEVER start with the executive cohort; earn it with results from the lower rungs.
