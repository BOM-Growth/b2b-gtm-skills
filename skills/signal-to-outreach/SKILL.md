---
name: signal-to-outreach
title: Signal to outreach
description: |
  Use this skill when a buying signal fires: a new follower from an ICP account, an
  identified website visitor, a prospect mentioned on a customer call, a job posting for
  the role we sell to, a competitor mention. Triggers on "new followers", "website
  visitors", "someone from X was on the site", "we have the signal", "turn signals into
  outreach". Produces a resolved, ICP-checked, deduped list of signal leads with the
  signal attached and the right small sequence for each.
collection: first-customers-and-outbound
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 3-strategy/funnel.md, 1-context/stack.md]
related: [outbound, outbound-cohort, outbound-sequence-copy, icp-fit-check, reply-handling]
playbook: 9
stage: distribution
---

This applies continuously. It produces warm outreach from intent the company can already see, instead of a single automated email nobody manages.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Load `gtm-context` and `1-context/stack.md` for where signals arrive: follower notifications, visitor identification alerts, call transcripts, job boards.
2. Resolve each signal to a person and a company. A visitor alert with a company and no person needs the champion persona found; a follower needs the company checked.
3. Gate: run `icp-fit-check`. Drop internal, customers (route to success), competitors, vendors. Dedupe against active pipeline and recent sends.
4. Attach the signal to the record as the angle: the page they visited, the post they followed from, the thing said on the call.
5. Write a short sequence per signal type through `outbound-sequence-copy`: three touches, the first referencing the signal plainly ("you were looking at the pricing page"), one ask. A single email is not a test of the channel.
6. Route: followers can be handled manually by a rep with the right account; visitors and call mentions go into the sequence tool. Volume decides automation: measure weekly signal counts before building any.
7. Report signals, outreach sent and demos booked by signal type in `weekly-marketing-update`.

## What good looks like

- The best operator gives a signal channel a fair test: a real sequence, a named owner, four weeks. One unmanaged email is not a test.
- The mediocre version pollutes the CRM with unresolved company names and anonymous visits.
- Good output is a small weekly list where every row has a person, a signal and a next touch, and nothing anonymous reached the CRM.

## Rules

- MUST resolve a signal to a person and pass the ICP gate before any CRM write.
- MUST attach the signal to the outreach as the angle.
- NEVER write anonymous or unresolved visitors to the CRM.
- NEVER judge a signal channel on a single-email test.
