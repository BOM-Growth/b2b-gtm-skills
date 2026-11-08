---
name: referral-partners
title: Referral and partners (playbook)
description: |
  Entry point for word of mouth and partner channels: "referral program", "refresh
  the referral program", "the reward", "who referred", "partner leads", "lead sharing", "co-marketing
  with", "joint webinar", "joint event". Routes the referral send, tracking and payout,
  and the partner lead exchange and co-marketing plays.
collection: referral-and-partners
type: playbook
reads: [2-standards/proof-rules.md, 1-context/stack.md, 3-strategy/funnel.md]
related: [referral-campaign, referral-tracker, partner-lead-exchange, co-marketing-campaign]
playbook: 19
stage: distribution
---

This applies to the two channels that run on other people's trust. It produces a referral program that is live and tracked, and partner relationships with a measurable lead flow both ways.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the referral terms (reward, eligibility, who can refer) and the partner list with each partner's scope.
2. Referral:
   - Launch or refresh → `referral-campaign` (audience, suppression, dedupe, reward structure, the one-click intro).
   - Any time → `referral-tracker` (who referred, stage reached, payout owed, pipeline from referrals).
   - Set the quarter's target in deals and pipeline, not in clicks.
3. Partners:
   - A partner that will share leads → `partner-lead-exchange` (a reciprocal SLA, reviewed on a cadence, with the check that both sides deliver).
   - A partner to build with → `co-marketing-campaign` (joint content, a shared event presence, shared costs).
4. Every referred or partner lead enters the CRM with its source and goes through `inbound-triage` the same day.
5. Monthly: referrals and partner leads by source into `weekly-marketing-update`; partners that miss their SLA twice get a conversation, not a third chance.

## KPIs

- Referred demos and deals per quarter; pipeline from referrals.
- Partner leads delivered and received per period against the SLA.
- Time from referral intro to first response.

## What good looks like

- The best operator makes referring take one click and pays out visibly. A program nobody can explain in one sentence does not get used.
- The mediocre version launches the page and never follows up on the intros, so the first referrer's experience is silence.
- Good output is a referral send that lands in users' inboxes with a live tracker behind it, and a partner SLA with a number both sides can check.

## Rules

- MUST clear the suppression list with customer success before any referral send to users.
- MUST record the referrer on every referred lead so payouts can be honored.
- NEVER send the same person the same ask twice in a cycle.
- NEVER promise a reward the terms do not state.
