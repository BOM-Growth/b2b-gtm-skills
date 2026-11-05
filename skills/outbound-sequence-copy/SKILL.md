---
name: outbound-sequence-copy
title: Outbound sequence copy
description: |
  Use this skill when a cohort needs words: "write the sequence", "cold email for",
  "follow-up emails", "the win-back email", "call script for the exec rung", "beat up
  this sequence". Produces the full sequence (every touch, subject lines, call notes)
  for one cohort and persona, from the context messaging and objections, with every
  proof point cleared.
collection: first-customers-and-outbound
type: play
reads: [1-context/personas.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md, 1-context/ideal-customer.md]
related: [outbound, outbound-cohort, brand-voice, permission-check, reply-handling]
playbook: 9
stage: distribution
---

This applies once a cohort is defined. It produces copy that sounds like a person who knows the prospect's work, not a vendor who found their email.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Take the cohort brief from `outbound-cohort`: who, angle, persona rung, size.
2. Pull the persona's pain, goal and top objection from `1-context/personas.md`, and the approved response to that objection.
3. Write touch one from the angle, in the first two lines. The reader should know why them and why now before the product is named.
4. Write the remaining touches, each with a different reason to reply: a peer's result (cleared), a question about their workflow, the objection answered, a short video or page, the last touch a plain close. No touch repeats the previous one.
5. Write subject lines as a person would type them, lowercase if that is how the persona writes. No slogans, no disclaimers ("no sales pitch"), no false questions.
6. Run every proof point and customer name through `permission-check`. Replace anything not cleared with role-only attribution.
7. For the manager and executive rungs, write the call notes: the opener, the one question, the ask.
8. Run `brand-voice` on the whole sequence for banned patterns and naming, then hand it to the sequence owner with the send schedule.

## What good looks like

- The best operator writes the first line last, after reading three of the prospect's own job postings, pages or posts. Specific beats clever.
- The mediocre version opens with the company's description of itself and asks for 15 minutes.
- Good output is a sequence where each touch would make sense arriving alone, and a prospect who replies "how did you know that" instead of "unsubscribe".

## Rules

- MUST lead with the cohort's angle, not the product.
- MUST clear every proof point through `permission-check`.
- NEVER use disclaimers, rhetorical questions or buzzwords; see `2-standards/proof-rules.md`.
- NEVER promise a feature above its maturity label.
