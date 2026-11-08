---
name: inbound-lifecycle
title: Inbound and lifecycle (playbook)
description: |
  Entry point for every hand-raise and every email the company sends to people it already
  knows: "a demo request came in", "triage this lead", "where did this lead come from",
  "attribution", "the routing form", "nurture email", "customer email", "the weekly
  send", "landing page for", "send me something to look at". Routes triage, routing,
  attribution, nurture, customer updates, landing pages and the leave-behind page.
collection: crm-and-tracking
type: playbook
reads: [1-context/ideal-customer.md, 3-strategy/funnel.md, 1-context/stack.md, 2-standards/proof-rules.md]
related: [inbound-triage, demo-routing, lead-source-audit, nurture-email, customer-update-email, landing-page-brief, leave-behind-page]
playbook: 8
stage: build
---

This applies to the demand the company already has. It produces a same-day response to every hand-raise, a source on every lead, and a weekly reason for in-pipeline contacts to come back.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the routing rules and the same-day SLA.
2. Every hand-raise: `inbound-triage` scores against the gates and routes to a demo; out-of-ICP hand-raisers get a polite path, not silence.
3. Keep the booking path honest with `demo-routing`: the form, the routing questions and the calendar it books into match the ICP and the sales capacity.
4. Monthly: `lead-source-audit` so every lead carries one first-touch source and the known gaps have an owner.
5. Weekly: `nurture-email` to in-pipeline contacts with one thing that moved (a release, an event, a customer story). Customers get `customer-update-email` first when something affects them.
6. When a play needs a page: `landing-page-brief` on the site's tracking rules, deployed through the site's own process.
7. Keep `leave-behind-page` current so a rep has one link to send when a prospect asks for something to look at.
8. Watch the two failure modes: leads that a workflow hides by mistake, and phone inquiries that never get logged. Both show up in `lead-source-audit`.

## KPIs

- Speed to first response on a hand-raise.
- Share of leads with a recorded first-touch source.
- Nurture send held weekly; replies and demos from nurture.

## What good looks like

- The best operator watches the hand-raisers nobody responded to. A slow quarter can be a routing problem, not a demand problem.
- The mediocre version has a demo form that promises one thing and a sales process that delivers another, and nurture that goes out when someone remembers.
- Good output is every inbound lead with a source, a same-day response, and a weekly send that in-pipeline contacts reply to.

## Rules

- MUST respond to every hand-raise within the SLA in `3-strategy/funnel.md`, including out-of-ICP ones.
- MUST send customers news before prospects when it affects them.
- NEVER compare paid channels on their own conversion definitions inside this playbook; use `3-strategy/funnel.md`.
- NEVER let a nurture send go out with an uncleared claim or customer name.
