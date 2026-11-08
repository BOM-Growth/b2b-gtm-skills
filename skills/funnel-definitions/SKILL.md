---
name: funnel-definitions
title: Funnel definitions
description: |
  Use this skill whenever a number's meaning is in question: "what counts as an MQL",
  "define SQL", "why do sales and marketing numbers differ", "is a demo request a
  lead", "the stage definitions", "set up the funnel fields". Produces the agreed
  definition per stage (entry rule, exit rule, owner, field in the CRM, SLA), the
  mapping from every lead source into the stages, and the reconciliation when two
  teams count differently.
collection: crm-and-tracking
type: play
reads: [3-strategy/funnel.md, 1-context/stack.md]
related: [reporting-experiments, weekly-marketing-update, lead-source-audit, inbound-triage, demo-routing, gtm-context]
playbook: 8
stage: build
---

This applies once to set the definitions and whenever a count is disputed. It produces one set of words for the funnel that marketing, sales and leadership all use.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Read the current definitions in `3-strategy/funnel.md`; where none exist, draft them with the template in `references/definitions-template.md`.
2. Per stage: the entry rule (what event or field moves a record in), the exit rule (forward or out), the owner, the CRM field and value, the SLA to the next stage. A rule must be testable from the record alone.
3. Map every source into the stages: a web demo request enters at the demo request stage; an event scan enters as a lead and needs a qualification step; a referral enters with the referrer's note; an outbound reply enters at the stage its intent shows.
4. Reconcile disputes: pull the records both teams count, apply the rules, show which records each side included and why. The rule changes only by a logged decision through `decision-log`.
5. Write the definitions into `3-strategy/funnel.md` and the CRM's field help text. Hand the field changes to the CRM owner.
6. Re-check quarterly in `quarterly-gtm-plan`; a stage nobody moves records through is a stage to remove.

## What good looks like

- The best operator writes a rule a new rep can apply to a record without asking anyone.
- The mediocre version defines a stage as "sales accepted" and leaves "accepted" to taste.
- Good output is a `3-strategy/funnel.md` the weekly update, the triage and the routing all cite without a translation layer.

## Rules

- MUST make every rule testable from the CRM record.
- MUST log any definition change in `decision-log`.
- NEVER report a stage count while its definition is disputed without saying so.
- NEVER keep a stage with no owner.
