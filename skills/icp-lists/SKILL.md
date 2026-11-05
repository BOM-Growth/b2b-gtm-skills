---
name: icp-lists
title: ICP and lists (playbook)
description: |
  Entry point for anything about who we target: "review the ICP", "are we targeting the
  right accounts", "build a list for", "is this account a fit", "filter these leads",
  "tier my accounts", "who should we go after", "what's our TAM". Routes to the plays
  that score an account, build a list from the TAM, or sort a received list. Runs the
  quarterly ICP review.
collection: icp-and-wedge
type: playbook
reads: [1-context/ideal-customer.md, 1-context/personas.md, 3-strategy/funnel.md]
related: [icp-fit-check, build-target-list, audience-icp-filter, gtm-context]
playbook: 3
stage: foundation
---

This is the entry point for targeting. It produces the right play for the request and, once a quarter, the ICP review.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the gates, tiers and segments are current (last reviewed date).
2. Classify the request:
   - One account, "is it a fit" → `icp-fit-check`.
   - A list to build for a play (event, association, ad audience, outbound cohort) → `build-target-list`.
   - A list we received (event scans, webinar signups, members, a partner's leads) → `audience-icp-filter`.
   - "Is the ICP right" or the quarterly review → steps 3 to 6.
3. Quarterly review: pull the quarter's closed won and churned accounts and score each against the gates. Note where winners failed a gate (the gate is too tight) and where churn passed every gate (a gate is missing).
4. Check lead quality: share of MQLs inside the gates, by channel. A channel sending mostly out-of-ICP leads is a targeting problem for that channel's play.
5. Propose gate changes with the evidence, and any segment to add or retire. Hand the decision to the ICP owner; log it with `decision-log`.
6. Push the result to the CRM owner so the gates are operationalized as fields and views, not left in a document.

## KPIs

- Share of MQLs inside the ICP gates, by channel.
- Share of closed won inside the gates.
- Churned accounts outside the gates (a high share means the gates are working).

## What good looks like

- The best operator reads churn as the sharpest ICP signal. If most churn is outside the gates, the gates are right and the leak is upstream.
- The mediocre version tightens the ICP to improve conversion rates and starves volume. Trading a point of conversion for ten times the volume is often the right call; the review should say which trade it is making.
- Good output is a one-page review with the gates kept, changed or added, each with the accounts that drove it.

## Rules

- MUST start every list from the TAM and the gates in `1-context/ideal-customer.md`, never from a fresh definition in the prompt.
- MUST keep the small-account rule (land and expand, not disqualify) unless the owner changes it.
- NEVER change a gate inside a play; propose it here and log it.
