---
name: partner-lead-exchange
title: Partner lead exchange
description: |
  Use this skill when a partner will share leads: "set up lead sharing with", "they
  agreed to send us leads", "are they delivering", "what do we owe them", "the SLA
  with the partner". Produces the reciprocal SLA (what, how many, how often, in what
  form, who receives), the intake into the CRM with the partner as source, the delivery
  log both ways, and the review.
collection: referral-and-partners
type: play
reads: [1-context/ideal-customer.md, 3-strategy/funnel.md, 1-context/stack.md, 2-standards/proof-rules.md]
related: [referral-partners, audience-icp-filter, inbound-triage, co-marketing-campaign]
playbook: 19
stage: distribution
---

This applies when a non-competing company serves the same buyers. It produces a lead flow both sides can count.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the partner is not a competitor and which segment and persona they reach.
2. Write the SLA on one page: leads per period each way, what counts as a lead (a named person at an ICP account with a reason), the format and channel, who receives on each side, the review cadence, and what happens when a side misses twice.
3. Set intake: partner leads enter the CRM with the partner as source, run through `audience-icp-filter` and `inbound-triage` the same day. Out-of-ICP partner leads go back with the reason, so the partner learns the gates.
4. Set delivery: our leads to the partner come from a defined pool (accounts that need what the partner sells, found in discovery), cleared by the deal owner, delivered on the cadence.
5. Keep the delivery log both ways: period, promised, delivered, accepted, demos, deals. Review on the cadence with the partner contact.
6. Add joint marketing where the SLA works, through `co-marketing-campaign`.
7. Report partner leads and their outcomes in `weekly-marketing-update` by partner.

## What good looks like

- The best operator defines a lead before counting one. A lead count means nothing until both sides agree on what a lead is.
- The mediocre version trades spreadsheets of names and calls it a partnership.
- Good output is a log where the partner can see we delivered, and a quarterly number for partner-sourced pipeline.

## Rules

- MUST define what counts as a lead in the SLA before any exchange.
- MUST enter partner leads with the partner as source and triage them the same day.
- NEVER share a customer's name or details with a partner without the customer's agreement.
- NEVER keep exchanging with a partner that has missed the SLA twice without a conversation.
