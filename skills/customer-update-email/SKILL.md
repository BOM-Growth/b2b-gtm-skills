---
name: customer-update-email
title: Customer update email
description: |
  Use this skill for email to existing customers: "the monthly customer update", "the
  release notes email", "tell customers about", "the newsletter", "the product update
  email for". Produces the email draft: what shipped and why it matters for them, the
  one thing to try, the proof or peer story, the ask (referral, review, interview), with
  the segment and send window.
collection: email-and-lifecycle
type: play
reads: [2-standards/brand-voice.md, 2-standards/proof-rules.md, 5-current/calendar.md, 3-strategy/funnel.md]
related: [inbound-lifecycle, release-to-narrative, product-tip-series, referral-campaign, customer-interview, nurture-email]
playbook: 13
stage: distribution
---

This applies monthly and at every release. It produces the email customers read because it tells them what to do differently this week.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Take the month's releases through `release-to-narrative`; pick the one to three that change a customer's day.
2. Segment: all customers, a plan, a role, or the accounts on a feature. The tip and the ask change by segment.
3. Structure: the one change and why it matters in two sentences; how to use it in three steps or a short clip from `customer-video-cut`; a peer story cleared through `permission-check`; one ask (a referral through `referral-campaign`, a review, an interview through `customer-interview`); what is coming next only if the date is committed.
4. Draft under 250 words in `brand-voice`, from a named sender. Subject states the change.
5. Check the window against `5-current/calendar.md`; avoid slow periods and the week of an event the segment attends.
6. Hand the draft to the human or the configured tool to send after approval. Log the send in the content calendar.
7. Read replies and the ask's results the following week; replies go to the account owner the same day.

## What good looks like

- The best operator leads with the one thing a customer should try, in the customer's words for the problem it solves.
- The mediocre version lists every ticket closed this month.
- Good output is an email that produces replies and a few referrals, and that support can point to when a customer asks what changed.

## Rules

- MUST clear every peer story and number through `permission-check`.
- MUST have one ask at most.
- NEVER send; the human or approved automation sends.
- NEVER announce a date that is not committed.
