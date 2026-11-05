---
name: release-to-narrative
title: Release to narrative
description: |
  Use this skill when a feature ships, is about to ship, or appears on the roadmap and
  marketing needs to know what it may say about it: "what can we say about X", "is this
  newsworthy", "write up the release", "what's the story on the new feature", "what's
  what changed for the customer". Produces the narrative (what could not be done before, what can be
  done now, who it is for), the maturity label, the cleared claims, and the channels and
  audiences it should reach.
collection: launch
type: foundation
reads: [2-standards/proof-rules.md, 1-context/personas.md, 1-context/stack.md]
related: [launch-calendar, customer-update-email, product-tip-series, decision-log]
playbook: 18
stage: distribution
---

This applies to every release that could be marketed. It produces the one page sales, success and marketing all read before anyone talks about the feature.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Read the release record named in `1-context/stack.md` for what shipped, what is in beta, and what is only demoed.
2. Assign the maturity label from `2-standards/proof-rules.md` (for example In development, Ready for demo, Ready for testing, General availability). The label decides what may be promised.
3. Write what changed for the customer in three lines: what the customer could not do before, what they can do now, what it means for the persona who feels it most (see `1-context/personas.md`).
4. List the limits a user will hit and the job types it does not cover. These go to sales and success, and they shape what marketing leaves out.
5. Decide newsworthiness: does it change what a prospect can do, answer a known objection, or open a segment? If yes, it feeds `launch-calendar`. If not, it feeds `product-tip-series` and `customer-update-email`.
6. Write the talk track: one headline, three supporting lines, the proof that may be used (through `permission-check`), the objection it answers.
7. Name the audiences: existing customers first, then in-pipeline contacts, then the market.
8. Log the decisions (label, claims, audiences) with `decision-log`.

## What good looks like

- The best operator writes the "before" first. A feature only lands when the reader recognizes the manual work it removes.
- The mediocre version describes the feature in the product's own words and overpromises the roadmap. Customers then hit the limit the page never mentioned.
- Good output lets a salesperson, a success manager and a marketer say the same thing about the feature, with the same label and the same limits.

## Rules

- MUST carry the maturity label on every claim and never give a ship date for anything not generally available.
- MUST send customers the news before the market sees it.
- NEVER describe a demoed capability as shipped.
- NEVER restate a customer's number as a company claim.
