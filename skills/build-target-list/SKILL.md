---
name: build-target-list
title: Build target list
description: |
  Use this skill when a play needs accounts or contacts: "build a list for the show",
  "who's in the association", "ad audience for", "this week's cohort", "target accounts
  in Texas", "everyone in the TAM who", "contacts at these companies". Produces a list
  from the TAM and the ICP gates with tier, segment, persona, source and dedupe status
  on every row, ready for the CRM, a sequence or an ad platform.
collection: icp-and-wedge
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 1-context/stack.md]
related: [icp-lists, outbound-cohort, event-outreach, association-play, linkedin-ads]
playbook: 3
stage: foundation
---

This applies whenever a play needs names. It produces a list that started from the TAM, not from a search box.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Identify the play the list serves and its filters (region, segment, tier, association membership, event attendance, persona).
2. Start from the TAM list named in `1-context/stack.md`. Apply the gates and the play's filters. Never start from a fresh search of the whole market when a TAM exists.
3. Enrich contacts by persona: for each account, the champion persona first, then the ladder from `1-context/personas.md`. Verify emails and roles with the enrichment tool in `1-context/stack.md`.
4. Dedupe against the CRM: active pipeline, customers, recent sends (30 days), do-not-contact, competitors and vendors.
5. Add the columns every downstream play needs: tier, segment, persona, source of the account (TAM, association, event), source of the contact, verification status.
6. Size the list against the play's capacity: a sequence owner's calendar, an ad audience's minimum size, a booth team's meeting target. Cut or split rather than overload.
7. Record where the list came from and when, so the next run can refresh it instead of rebuilding.

## What good looks like

- The best operator checks the list against capacity before quality. A perfect list of 1,200 contacts a one-person sales team cannot follow up is a worse list than 150 they can.
- The mediocre version pulls a fresh export with every request and ends up with three TAMs that disagree.
- Good output is a list where every row says why it is there and how it was verified, and no row is already in the pipeline.

## Rules

- MUST start from the TAM and the gates in `1-context/ideal-customer.md`.
- MUST dedupe against active pipeline, customers and recent sends.
- NEVER include contacts at competitors or vendors in an outbound list.
- NEVER buy attendee lists; use organizer, exhibitor, member and past-attendee sources.
