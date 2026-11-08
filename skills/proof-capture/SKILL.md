---
name: proof-capture
title: Proof capture
description: |
  Use this skill the moment proof appears: a quote on a call, a video testimonial
  submitted, a number a customer shares, a positive line in an email, a
  review. Triggers on "add this to the quote bank", "they said something great on the
  call", "a testimonial came in", "file this quote", "what proof do we have on X".
  Produces the tracker row (customer, person, quote or number, source, date, channels
  approved, status) and the pending-review list.
collection: content-and-proof
type: play
reads: [2-standards/proof-rules.md, 1-context/stack.md]
related: [content-proof, permission-check, case-study, customer-interview, customer-video-cut, decision-log]
playbook: 10
stage: distribution
---

This applies continuously. It produces a proof bank that is current, so a few customers do not carry every piece.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the permissions tracker in `1-context/stack.md`.
2. Capture the proof as said: the words, the number with its caveat, who said it, their role, the company, the date, the source (call id, video, email, booth, review site).
3. Classify: quote, number, logo use, story, video. Note which channels it could serve.
4. Set status: pending customer review for anything not yet approved; approved only when the customer has seen the exact words and the channels.
5. Write the row to the tracker. Link the recording or message. Never keep quotes in a document outside the tracker.
6. Keep the pending list and chase it through the relationship owner, batched, not one email per quote.
7. On a request for proof ("what do we have on results"), answer from the tracker only: approved rows with their channels, or "nothing approved yet" with the pending candidates.
8. Retire rows when a customer churns or withdraws; mark, do not delete.

## What good looks like

- The best operator files the quote the day it is said, with the recording link. A quote remembered a month later is a paraphrase.
- The mediocre version keeps quotes in a slide deck and nobody knows which are approved.
- Good output is a tracker where every row answers "can we use this, where" in one glance.

## Rules

- MUST record proof with its source and date the day it appears.
- MUST keep status pending until the customer has approved the exact words and channels.
- NEVER store quotes or attributions anywhere but the tracker.
- NEVER mark approved on the strength of prior use.
