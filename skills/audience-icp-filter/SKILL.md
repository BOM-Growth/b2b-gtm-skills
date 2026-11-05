---
name: audience-icp-filter
title: Audience ICP filter
description: |
  Use this skill when a list already exists and someone needs to know who on it is worth
  contacting: event scans, webinar registrants, an association member list, a partner's
  leads, a newsletter export. Triggers on "filter this list", "who here is a fit", "clean
  up these leads", "qualify the signups", "did we scan junk", "sort the scans". Produces
  every row sorted into match, review or no match with a reason, colleagues and
  competitors stripped out, nobody dropped silently.
collection: icp-and-wedge
type: play
reads: [1-context/ideal-customer.md, 3-strategy/funnel.md]
related: [icp-lists, event-lead-ingest, icp-fit-check, partner-lead-exchange]
playbook: 3
stage: foundation
---

This applies to any list the company received rather than built. It produces three piles and a reason on every row.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Note where the list came from and what the person on it did (scanned a badge, registered, is a member).
2. Normalize: company name, domain, person, title, source event. Merge duplicates.
3. Strip internal colleagues, competitors, vendors selling to us, event staff and media. Keep them in a separate sheet, not deleted.
4. Score each row against the gates. Match: passes every known gate. Review: an unknown on a gate, or a known adjacent segment. No match: fails a hard gate.
5. Write the reason on every row in a few words ("wrong industry", "adjacent segment", "scale unknown").
6. For match and review rows, add the persona and the recommended next step from the play that owns the list (event follow-up tier, nurture, decline politely).
7. Return counts by pile and by source, so the play owner can see the list's quality at a glance.

## What good looks like

- The best operator keeps the no-match rows and says why. "We dropped 40%" with no reasons gets the list rebuilt by someone who does not trust it.
- The mediocre version keeps only the obvious matches and loses the review pile, where the land-and-expand accounts live.
- Good output is the same list back with three new columns (pile, reason, next step) and a count table on top.

## Rules

- MUST keep every input row in the output, in one of the three piles.
- MUST write a reason on every row.
- NEVER contact a stripped row (colleague, competitor, vendor).
- NEVER promote a review row to match without a confirmed gate value.
