---
name: event-outreach
title: Event outreach
description: |
  Use this skill in the eight weeks before a show: "book meetings before the show",
  "who do we email about the show", "pre-show campaign", "the booth draw", "attendee
  list outreach", "tell customers we'll be there", "open deals at the show". Produces the
  four lists (targets, attendees, open pipeline, customers), the pre-booked meeting
  target, the booth draw, the email and posting cadence, and the owner per list.
collection: events
type: play
reads: [5-current/calendar.md, 1-context/ideal-customer.md, 1-context/personas.md, 2-standards/brand-voice.md, 2-standards/proof-rules.md]
related: [events, event-plan, build-target-list, audience-icp-filter, social-post, nurture-email]
playbook: 14
stage: distribution
---

This applies from eight weeks out to the show. It produces the meetings that make the show pay before the doors open.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Load `gtm-context` and `5-current/calendar.md`: the pre-booked meeting target and the booth draw deadline.
2. Build four lists, each with an owner:
   - Targets: ICP accounts in the show's region or segment from `build-target-list`, filtered to those likely to attend.
   - Attendees: the organizer's list when it arrives, or exhibitor, member and past-attendee company lists, run through `audience-icp-filter`.
   - Open pipeline: every deal whose contact may attend; the deal owner books an in-person meeting.
   - Customers: users and contacts to meet for renewals, feature intros and advocacy on the booth.
3. Pick the booth draw by the deadline: something that pulls a buyer into the booth and ties to a demo (a live run on their own material, a customer at the booth, a short session). Name it in every send.
4. Set the cadence: announce four weeks out; two posts a week at two to three weeks; daily in the final week; three pre-show emails to the attendee list; one to open pipeline; one to customers.
5. Write the emails and posts through `brand-voice`, proof through `permission-check`. One ask per email: book a time.
6. Track meetings booked against the target weekly; add a customer advocate to the booth schedule if one agrees.
7. Hand the booked meetings and the lists to `event-prep-deck` and `event-lead-ingest`.

## What good looks like

- The best operator counts booked meetings, not emails sent, and knows by week two whether the show will hit its target.
- The mediocre version sends one "visit us at booth 1234" email the week before.
- Good output is a show the team walks into with the meeting target met, a customer on the booth, and a draw every attendee has already heard about.

## Rules

- MUST set and track a pre-booked meeting target.
- MUST source lists from organizer, exhibitor, member and past-attendee sources; never buy them.
- NEVER email a customer about the show without checking their health status with success.
- NEVER name a draw you cannot deliver on the booth.
