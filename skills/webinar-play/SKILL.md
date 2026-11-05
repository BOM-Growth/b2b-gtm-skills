---
name: webinar-play
title: Webinar and hosted event
description: |
  Use this skill for events the company hosts: a webinar, a dinner near a show, a
  workshop, a customer session. Triggers on "run a webinar", "host a dinner", "steak
  dinner for local buyers", "customer workshop", "lunch and learn". Produces
  the invite list, the offer, the format, the run of show, the capture and the follow-up
  plan, sized to produce a stated number of qualified conversations.
collection: events
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 5-current/calendar.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md]
related: [events, build-target-list, event-lead-ingest, event-follow-up, customer-launch-kit]
playbook: 14
stage: distribution
---

This applies when the company wants the audience in a room it controls. It produces a small event with a clear target and a follow-up, not a broadcast.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). State the target in qualified conversations, not registrations, and the region or segment.
2. Pick the format against the target: a dinner for a dozen Tier 1 accounts near a show; a webinar for a segment with a customer presenting; a workshop for existing customers around a release.
3. Build the invite list with `build-target-list` (prospects) and with success (customers who can anchor the room). A customer host doubles acceptance.
4. Write the offer and the invite in `brand-voice`: the problem the session addresses, who else will be there, one ask. Three touches, the last a personal note from the host.
5. Write the run of show: a customer or founder on the problem, the approach, a short live run on real material, questions. The product is shown in the middle, not the opening.
6. Capture attendance and questions as leads through `event-lead-ingest`, source = the event name. Questions asked are the scan notes.
7. Follow up through `event-follow-up`: attendees as warm, registrants who did not attend as cold with the recording.
8. Debrief with `event-debrief` at the same horizon as a show.

## What good looks like

- The best operator makes the room small and the host a customer. Twelve buyers at a dinner outperform three hundred webinar registrants nobody follows up.
- The mediocre version runs a product webinar to a cold list and counts registrations.
- Good output is a guest list the sales team is excited about, a customer at the front of the room, and a follow-up view a week later.

## Rules

- MUST state the target in qualified conversations before inviting anyone.
- MUST capture every attendee and question as a lead with the event as source.
- NEVER open with the product; open with the audience's problem.
- NEVER invite a customer to host without clearing it with success.
