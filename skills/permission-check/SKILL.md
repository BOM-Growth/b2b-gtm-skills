---
name: permission-check
title: Permission check
description: |
  Use this skill before any customer name, logo, quote, number or story appears in a piece,
  and when someone asks "can we use X", "is this quote approved", "can we name them",
  "is that number cleared". Produces a yes or no for that customer, that piece and that
  channel, with the tracker row it came from, or the attribution-by-role fallback.
collection: content-and-proof
type: foundation
reads: [2-standards/proof-rules.md, 1-context/stack.md]
related: [gtm-context, proof-capture, case-study]
playbook: 10
stage: distribution
---

This applies to every content, outbound, event and ad skill at the moment a customer is about to be named. It produces a decision and the fallback wording when the answer is no.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Find the permissions tracker named in `1-context/stack.md`.
2. Identify every customer-specific element in the draft: name, logo, quote, number, story, photo, title.
3. For each, look up the tracker row. Check three things: the customer is approved, the element type is approved (quote versus logo versus number), and the channel and piece type are approved (a case study approval is not a paid ad approval).
4. For a number, apply the customer-stated rule in `2-standards/proof-rules.md`: credited to the customer and in their words is fine; restated as a company claim is not.
5. For a quote, allow light cleanup of spoken words. Flag anything that changes the meaning or could embarrass the customer.
6. If any check fails, return the role-only attribution ("a mid-size [segment] company") and the cleared company claims that could stand in.
7. If the customer is a churn risk or has churned, say so and recommend swapping them out even where the tracker says yes.
8. Record what was checked in one line so the piece can carry it to review.

## What good looks like

- The best operator checks the channel, not just the customer. Most permission failures are a cleared case study quote reused in an ad or an outbound email the customer never agreed to.
- The mediocre version asks "have we used this before" and treats prior use as permission. Prior use is how uncleared quotes spread.
- Good output lists each element with its tracker row or its fallback, and the piece ships with nothing unchecked.

## Rules

- MUST treat "not in the tracker" and "not approved for this piece and channel" as no.
- MUST keep customer-stated numbers credited to the customer; the company makes no general claim from them.
- NEVER soften a no into "probably fine". Return the fallback wording instead.
- NEVER ask the customer to supply logos or headshots; pull them from public sources and ask the customer to confirm they are the right ones.
