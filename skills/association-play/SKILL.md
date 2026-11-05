---
name: association-play
title: Association play
description: |
  Use this skill for regional and trade associations: "join the association", "their
  meeting is next month", "get on their member list", "who runs the association", "speak
  to their members", "they want us to come speak", "we're caught flat-footed on these
  events". Produces the ranked association list, the discovery chat plan, the offer to
  members, the meeting attendance plan and the speaking ask, with a person assigned to
  each meeting worth attending.
collection: events
type: play
reads: [1-context/ideal-customer.md, 5-current/calendar.md, 1-context/personas.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [events, build-target-list, speaking-proposal, event-lead-ingest, outbound-cohort]
playbook: 14
stage: distribution
---

This applies to the long tail of industry gatherings a vertical company cannot ignore. It produces presence where buyers already meet, at a fraction of a trade show's cost.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Scrape or list the associations in the market: name, region, member count, members in our TAM, customers who are members, meeting dates, who runs it. Keep it in the TAM tool named in `1-context/stack.md`.
2. Rank by members in the TAM and by current ARR from members. Customers on an association's board are the way in.
3. For each association worth working, book a discovery chat with the person who runs it. Do not pitch. Ask what their members need, offer a talk on the industry topic the company knows (not the product), and ask how the association shares vendor offers with members.
4. Craft the member offer with sales: something a member can take up alone (a free run on their own material, a first-project credit) with a clear next step into a scoping call. It does not have to scale; it has to produce a handful of leads.
5. Get on the member list: the association's newsletter, the meeting invite list, the sponsor directory.
6. For meetings in the next quarter, send one person for a day or two where the TAM count justifies it; otherwise engage digitally with the offer. Name the person and the date in the events system of record. Meeting leads go through `event-lead-ingest`.
7. Ask for the speaking slot through `speaking-proposal` for the next meeting cycle.
8. Review quarterly: members in TAM reached, leads, meetings attended, ARR from members.

## What good looks like

- The best operator leads with a talk the association wants, not with the product. Associations are starved for speakers and wary of vendors.
- The mediocre version emails the association a sponsorship ask and hears nothing.
- Good output is a ranked list with a person and a date against the top few, a standing offer their members have seen, and a speaking slot booked for the next cycle.

## Rules

- MUST rank by TAM members and current customers, not by association size.
- MUST hold the discovery chat before any offer or sponsorship ask.
- NEVER pitch the product in the first conversation with an association.
- NEVER send someone to a meeting without a member list and the offer in hand.
