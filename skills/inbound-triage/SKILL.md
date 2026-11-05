---
name: inbound-triage
title: Inbound triage
description: |
  Use this skill on every inbound lead: "a demo request came in", "triage the inbound",
  "is this lead real", "who should take this", "the form submissions this week".
  Produces the triage record per lead: fit against the gates, intent, source, the
  action (route to a rep, nurture, decline with a referral), and the SLA clock.
collection: crm-and-tracking
type: play
reads: [1-context/ideal-customer.md, 3-strategy/funnel.md, 1-context/personas.md, 1-context/stack.md]
related: [inbound-lifecycle, icp-fit-check, demo-routing, nurture-email, lead-source-audit, closed-lost-winback]
playbook: 8
stage: build
---

This applies to every lead, same day. It produces a decision per lead and keeps the demo request pipeline clean enough to report on.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the new leads from the CRM in `1-context/stack.md`: form submissions, event scans, referral submissions, partner handoffs, replies to outbound.
2. Run `icp-fit-check` on each: company against the gates, person against the personas. Record the tier and any gate that fails.
3. Read the intent: what they asked for, what page they came from, what they wrote in the form. A demo request from a fit account is a different lead from a pricing question from a student.
4. Decide: route (fit and intent) through `demo-routing`; nurture (fit, low intent) through `nurture-email`; decline with a referral (not fit) with a courteous reply draft; park (unclear) with the one question that resolves it.
5. Check for an existing account or a closed-lost record; a returning account goes to its prior owner and to `closed-lost-winback` context.
6. Set the SLA clock from `3-strategy/funnel.md` and the source: an event lead in the Hot window, a web demo request same business day. Flag any lead already past it.
7. Log the triage on the record: tier, intent, action, owner, SLA. Report the week's counts and misses in `weekly-marketing-update`.

## What good looks like

- The best operator reads the form text and the referrer before the company name. Intent decides the action; fit decides the owner.
- The mediocre version routes everything with an email address to the next rep in the rotation.
- Good output is every lead with a decision and an owner the same day, and a weekly count of what came in by source and fit.

## Rules

- MUST run `icp-fit-check` on every lead before routing.
- MUST set the SLA clock from `3-strategy/funnel.md`.
- NEVER discard a lead without a logged reason and a reply draft.
- NEVER contact the lead from this skill; the owner does.
