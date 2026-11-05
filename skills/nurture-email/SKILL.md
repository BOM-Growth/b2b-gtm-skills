---
name: nurture-email
title: Nurture email
description: |
  Use this skill for the emails to leads who are not ready: "the nurture sequence", "what
  do we send the leads who didn't book", "the post-webinar sequence", "the event leads
  that went cold", "a drip for", "re-engage the old leads". Produces the sequence (goal,
  trigger, exit, each email's job), the email drafts with cleared proof, and the metrics
  to read it on.
collection: email-and-lifecycle
type: play
reads: [1-context/personas.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md, 3-strategy/funnel.md, 5-current/calendar.md]
related: [inbound-lifecycle, inbound-triage, customer-update-email, content-calendar, case-study, product-tip-series, closed-lost-winback]
playbook: 13
stage: distribution
---

This applies whenever a cohort of leads is fit but not ready. It produces a sequence that teaches, proves and asks once, in the company's voice.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Define the cohort, the trigger (form, event, webinar, cold outbound reply, closed-lost after six months), the goal (a booked demo) and the exit (booked, replied, unsubscribed, bought).
2. Plan the sequence by job, not by count: one email that names the problem in the persona's words, one that proves it with a cleared customer story, one that shows the product doing the job (a tip from `product-tip-series` or a screenshot), one that asks. Four to six emails over four to eight weeks for a considered purchase.
3. Pull proof through `permission-check`; the case study and quote come from the tracker exactly as cleared.
4. Draft each email: a subject that states the point, under 150 words, one link, one ask or none. Plain text style; the founder's name where `founder-voice` fits the cohort.
5. Run `brand-voice`. Check the send windows against `5-current/calendar.md`; pause over the dead zone.
6. Build the exit rules and the handoff: a reply or a booking goes to `inbound-triage` the same day.
7. Read it monthly on replies and booked demos per cohort, not on opens. Retire an email that produces neither after two cohorts.

## What good looks like

- The best operator writes the sequence a buyer would forward to a colleague.
- The mediocre version sends a product newsletter five times with a different subject line.
- Good output is a sequence where each email has a job, and the readout says which ones did it.

## Rules

- MUST define the exit before the first send.
- MUST clear every proof point through `permission-check`.
- NEVER send; the human or the configured automation sends after approval.
- NEVER judge the sequence on open rate.
