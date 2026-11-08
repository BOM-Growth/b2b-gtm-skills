---
name: icp-fit-check
title: ICP fit check
description: |
  Use this skill when one account needs a verdict: "is this a fit", "should we take
  this demo", "tier this account", "is this company in our ICP", "they're small, do we
  still want them", "check them against the TAM". Produces a pass or fail on each gate,
  a tier, the segment, the discovery signals still to confirm, and the recommended play.
collection: icp-and-wedge
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md]
related: [icp-lists, inbound-triage, build-target-list, audience-icp-filter]
playbook: 3
stage: foundation
---

This applies to one account at a time. It produces a verdict a rep can act on in the next call.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). List the gates with their values.
2. Pull what the CRM already holds on the account, then public sources (site, directory listings, job postings, industry memberships). Note the source of each fact.
3. Score each gate pass, fail or unknown. An unknown is not a fail; it becomes a discovery question.
4. Assign the tier from the tier table. Name the segment if the account is not in your main one.
5. Apply the small-account rule: an account that passes every gate except size starts small and grows. It is not a decline.
6. List the discovery signals from `1-context/ideal-customer.md` still to confirm on the call, and the persona most likely to champion from `1-context/personas.md`.
7. Recommend the play: targeted outreach, the normal demo path, the lower-touch path, or decline with the polite exit and the referral ask.
8. Write the verdict back to the CRM fields the gates map to.

## What good looks like

- The best operator separates "fails a gate" from "we don't know yet" and sends the unknowns to discovery instead of guessing.
- The mediocre version disqualifies on headcount or revenue alone and misses the small team that does a lot of volume.
- Good output fits on one card: gates, tier, segment, three discovery questions, the play.

## Rules

- MUST cite the source for each gate fact.
- MUST treat unknowns as discovery questions, not failures.
- NEVER decline an account inside the gates because it is small; route it to the lower-touch path.
- NEVER change a gate value here.
