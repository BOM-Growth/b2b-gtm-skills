---
name: customer-launch-kit
title: Customer launch kit
description: |
  Use this skill when a launch needs customers in it: "get customers posting on launch
  day", "customer quotes for the release", "co-marketing for the launch", "who can we
  ask to share", "the launch kit". Produces the customer list with permission status,
  the ask email, the ready-to-post copy per customer, the quote requests, and the day-of
  schedule, with success as the relationship owner.
collection: launch
type: play
reads: [2-standards/proof-rules.md, 2-standards/brand-voice.md, 1-context/stack.md]
related: [launch, launch-calendar, permission-check, proof-capture, case-study]
playbook: 18
stage: distribution
---

This applies in the weeks before a launch. It produces customer voices on launch day without a single uncleared name.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the customer list from the CRM with health status; ask success to mark who is in a good place to be asked.
2. Run `permission-check` on each candidate for the pieces planned (a post, a quote, a logo, a video clip). Keep only cleared or clearable customers.
3. Write the ask in the success owner's voice: what is launching, what we are asking (share a post, give a quote, be named), what they get (early access, a feature in our channels), and the date. One ask per customer, sent by the person who owns the relationship.
4. Draft the ready-to-post copy per customer so saying yes costs them nothing. Keep it in their voice, not the company's; make it easy to edit.
5. Collect quotes with `proof-capture` so they enter the tracker with their permission status the day they arrive.
6. Build the day-of schedule: who posts when, who reshares, who thanks them.
7. After launch day, send the thank-you and log which customers took part, for the next ask.

## What good looks like

- The best operator asks fewer customers with a specific, easy request than many customers with a vague one. A customer who gets a drafted post and a date usually says yes.
- The mediocre version blasts the base with "please share our news" and gets nothing.
- Good output is a short list of customers, each cleared, each with a draft, each asked by the person they know.

## Rules

- MUST clear every customer through `permission-check` for each piece and channel before the ask.
- MUST route every ask through the relationship owner in success.
- NEVER draft a customer's post with a claim they did not state.
- NEVER ask a churn-risk or churning customer.
