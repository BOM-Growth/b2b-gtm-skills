---
name: decision-log
title: Decision log
description: |
  Use this skill when a GTM decision gets settled in a chat, a call or a review: a naming
  rule, a claim dropped, a price or incentive, a headline, a segment added, a channel paused.
  Produces a dated decision entry with its source, the pages it changes, and the open
  items it leaves. Triggers on "log that", "we decided", "settled", "going with", and
  whenever a skill run surfaces a conflict the person then resolves.
collection: marketing-brain
type: foundation
reads: [1-context/stack.md]
related: [gtm-context, daily-brain-sweep]
playbook: 2
stage: foundation
---

This applies the moment a decision is made. It produces an entry the next skill run will read, so the decision does not have to be made twice.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the decision is a decision: a named person settled it, not a suggestion that was not objected to.
2. Write the entry: date, who decided, the decision in one sentence, the reason in one sentence, the source (call, chat, review, with a link where one exists).
3. List the context files and knowledge base pages the decision changes. Propose the exact line change for each.
4. List what the decision leaves open, so it is not mistaken for settled.
5. If you can only suggest edits to the knowledge base, file the entry as a suggestion for the owner. If you may edit it directly, apply the line changes and the entry in the same change.
6. Check for an older decision the new one supersedes and mark the older one superseded, with the date.

## What good looks like

- The best operator records the reason, because the next person asks "why" before "what". A decision without a reason gets relitigated.
- The mediocre version logs the outcome of a meeting as a decision when it was a direction. Directions change weekly; decisions should not.
- Good output is one dated entry that a reader can act on without opening the source, plus the list of pages it touched.

## Rules

- MUST name the person who decided and the date.
- MUST mark superseded decisions rather than deleting them.
- NEVER log a suggestion, a draft direction or an unobjected-to idea as a decision.
- NEVER carry private meeting content into the entry; the decision and its reason only.
