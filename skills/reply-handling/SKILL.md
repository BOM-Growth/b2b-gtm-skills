---
name: reply-handling
title: Reply handling
description: |
  Use this skill when outbound replies come in: "they replied", "what do I say back",
  "interested but not now", "they asked for pricing", "out of office", "wrong person",
  "the calendar is full". Produces the reply classified, the drafted response or stop
  action, the CRM update (deal created at the first stage when a demo is booked), and
  the calendar overflow decision.
collection: first-customers-and-outbound
type: play
reads: [3-strategy/funnel.md, 1-context/personas.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [outbound, outbound-sequence-copy, inbound-triage, demo-routing]
playbook: 9
stage: distribution
---

This applies to every reply. It produces a next step within the day and a CRM that reflects it, without anything auto-sent.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the reply with its thread and the cohort angle it came from.
2. Classify: wants a meeting; interested, not now; question (pricing, feature, integration); referral to someone else; not a fit; unsubscribe; out of office; bounce.
3. For a meeting: draft the booking reply with the link to the right calendar; create the deal at the first pipeline stage; stop the sequence.
4. For not now: draft a one-line acknowledgment with a specific return date; set a task; stop the sequence; tag for `nurture-email`.
5. For a question: answer from context through `permission-check`; pricing questions go to the account executive with the thread, never answered from marketing.
6. For a referral: thank them, start the referred person as a new row in the cohort with the referrer named.
7. For not a fit, unsubscribe or bounce: stop, record the reason, update the suppression list.
8. Calendar overflow: if the booking calendar fills past the agreed load, route new bookings to a backup calendar and tell the sales lead.
9. Every draft goes to the sender for review; nothing is sent automatically. Log the classification counts for `weekly-marketing-update`.

## What good looks like

- The best operator reads "interested, not now" as a date to put in the calendar, not a polite no.
- The mediocre version lets replies sit in the sequence tool for days and answers pricing from the marketing seat.
- Good output is every reply classified and answered the same day, a deal for every booked demo, and no one left in a sequence after they replied.

## Rules

- MUST stop the sequence on any human reply.
- MUST create the deal at the first stage when a demo is booked, and nowhere earlier.
- NEVER auto-send a reply; drafts go to the sender.
- NEVER answer pricing from marketing; route to sales with the thread.
