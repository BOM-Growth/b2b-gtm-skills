---
name: referral-campaign
title: Referral campaign
description: |
  Use this skill to launch or refresh a referral program send: "relaunch referral",
  "blast the referral email", "the reward is now", "open it to non-customers", "make the
  intro one click", "who gets the referral email". Produces the audience with suppression
  cleared and duplicates removed, the reward structure stated once, the page and email
  copy, the one-click intro mechanism tested on the audience's mail client, and the send
  plan.
collection: referral-and-partners
type: play
reads: [2-standards/proof-rules.md, 2-standards/brand-voice.md, 3-strategy/funnel.md, 1-context/stack.md]
related: [referral-partners, referral-tracker, brand-voice, permission-check, nurture-email]
playbook: 19
stage: distribution
---

This applies at relaunch and each refresh. It produces a send that lands with the people most likely to refer and makes referring take one click.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the terms from `decision-log` or the program page: reward amount and structure (at demo, at close), who may refer (customers only, or anyone), end date.
2. Build the audience: product users, customer contacts, and if open to anyone, in-pipeline contacts and fans who are not customers. Combine the lists in the CRM; dedupe so nobody gets it twice.
3. Clear the suppression list with success: churn-risk accounts, open escalations, anyone success asks to hold. No send to a user until success has looked.
4. Write the page and the email through `brand-voice`: one headline with the reward, two lines on how it works, one button. If the audience includes non-customers, the copy must not say "as a customer".
5. Build the one-click intro: the button opens a prefilled email to the referrer's contact with the company copied. Test it on the mail clients the audience uses (desktop and web). If the email tool cannot render it as a button, use a link and say so.
6. Send to the smallest group first (users), read replies and intros for a day, then send to the wider list. If it lands flat with users, fix before widening.
7. Plan the cadence: a reminder at two weeks, a thank-you to referrers, a note when the end date nears. Hand every intro to `inbound-triage` the same day.
8. Record the send in `referral-tracker`.

## What good looks like

- The best operator makes the headline the reward and the action one click. Programs die on friction and vague terms.
- The mediocre version sends a long explanation of tiers to the whole list in one go, with a form that asks the referrer to do the work.
- Good output is an email a user can act on in ten seconds, with a tracker that catches the first intro the same day.

## Rules

- MUST clear the suppression list with success before any send to users.
- MUST dedupe across every list in the audience.
- NEVER state a reward the terms do not back.
- NEVER send the whole audience before the first group's result is read.
