---
name: lead-source-audit
title: Lead source audit
description: |
  Use this skill when the source numbers cannot be trusted: "where are leads coming
  from", "attribution is broken", "the source field is empty", "the form isn't tagging",
  "what did paid actually produce", "the CRM says direct for everything". Produces the
  audit of how source is captured at every entry point, the gaps, the fix list, and the
  corrected source table for the period.
collection: crm-and-tracking
type: play
reads: [3-strategy/funnel.md, 1-context/stack.md]
related: [inbound-lifecycle, funnel-definitions, paid-weekly-report, weekly-marketing-update, event-lead-ingest]
playbook: 8
stage: build
---

This applies quarterly and whenever a source number looks wrong. It produces a source field the weekly update can rely on.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). List every entry point: web forms, booking links, event scans, referral forms, partner handoffs, outbound replies, manual creates.
2. For each, trace how source is set: tracking parameters, hidden fields, form defaults, list imports, rep entry. Record what gets written and where it can be lost (a redirect, a booking tool, an import template).
3. Sample the period's leads. Classify each by the true source from the evidence (page, campaign, event list, referrer) and compare to the CRM field. Count the mismatches by entry point.
4. Rank the gaps by leads affected. Common ones: booking links that drop parameters, event imports with no source, reps creating records by hand, "direct" absorbing everything untagged.
5. Write the fix list: the field change, the form change, the import template, the rep rule. Assign each to an owner with a date. Route site changes through the deploy process.
6. Produce the corrected source table for the period and hand it to `weekly-marketing-update` and `paid-weekly-report` with the caveat on each row that was corrected by hand.
7. Re-sample next month to confirm the fixes held.

## What good looks like

- The best operator traces one lead end to end from the ad click to the CRM record before trusting any table.
- The mediocre version re-labels "direct" as "organic" and moves on.
- Good output is a source field that needs no hand correction next quarter.

## Rules

- MUST trace every entry point, not only the web forms.
- MUST mark hand-corrected rows as corrected.
- NEVER overwrite historical source values in the CRM without a logged reason.
- NEVER report a source number from this audit as final until the re-sample confirms it.
