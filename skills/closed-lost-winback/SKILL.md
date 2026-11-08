---
name: closed-lost-winback
title: Closed-lost win-back
description: |
  Use this skill when something has changed that answers a past objection: a release, a
  pricing change, a new package, a segment opened. Triggers on "re-engage closed lost",
  "win-back", "they said we were missing X and now we have it", "pricing campaign to old
  prospects", "call the lost deals". Produces the cohort grouped by lost reason,
  the angle per group, the sequence and call list, and the sales hand-off.
collection: email-and-lifecycle
type: play
reads: [3-strategy/funnel.md, 1-context/personas.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [launch, outbound, outbound-cohort, outbound-sequence-copy, reply-handling]
playbook: 13
stage: distribution
---

This applies after a release or a pricing change. It produces the warmest cohort there is: people who already evaluated the product and said why they passed.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull closed-lost deals from the CRM for the last 12 months with their lost reason, the persona who said it, and the last contact.
2. Group by lost reason: missing feature, too small or budget, price, chose a competitor, timing. Drop reasons the change does not touch.
3. Match each group to what changed: the release answers a feature gap, the package answers budget, the new pricing answers price. Write the angle in one line per group: "you told us X was missing; here it is".
4. Rank groups by warmth and value: feature-gap losses first, then budget, then price. Competitor losses go to the end, and only where the change beats the competitor on the reason given.
5. Hand each group to `outbound-sequence-copy` with the angle, and to the sales owner for calls. Sales calls this cohort; it is a warm call, not a cold one.
6. Ask for a current example of the prospect's own data, whatever the product runs on, so the new demo uses their own example.
7. Track separately in `weekly-marketing-update`: reactivated deals and demos from win-back, by lost reason.

## What good looks like

- The best operator leads with the prospect's own words. "You said" beats any feature list.
- The mediocre version sends the launch announcement to the closed-lost list and calls it win-back.
- Good output is a short list, each account with the reason it passed and the one thing that changed, that a rep can call through in a week.

## Rules

- MUST use the lost reason recorded in the CRM, and ask sales where it is missing rather than guessing.
- MUST have sales make the calls; marketing supplies the list and the angle.
- NEVER promise a feature that is not ready for the way the prospect would use it.
- NEVER contact a lost deal whose reason the change does not address.
