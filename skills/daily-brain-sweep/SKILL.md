---
name: daily-brain-sweep
title: Daily brain sweep
description: |
  Run this loop every morning: "the morning sweep", "what changed overnight", "update
  the brain", "anything new from the calls yesterday". Reads yesterday's calls,
  messages, releases and replies, and produces the list of facts to add or change in
  the context files and the proof tracker, each with its source, for a human to
  approve. The brain stays current because this runs; the agents stay right because
  the brain is current.
collection: marketing-brain
type: loop
cadence: daily
reads: [1-context/stack.md, 2-standards/proof-rules.md, 5-current/calendar.md]
related: [gtm-context, permission-check, proof-capture, release-to-narrative, decision-log, weekly-channel-update]
playbook: 2
stage: foundation
---

This runs daily, first thing. It produces a short approval list, not a report; the point is that the context files never drift more than a day from reality.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The loop

1. Read the context (see Before you start). Pull yesterday's sources from `1-context/stack.md`: call recordings (full transcripts, never AI summaries), the team's messages in the marketing and sales channels, the release notes or merged changes, inbound replies, new leads, event tool updates.
2. For each item, ask one question: does this change a fact in a context file or the proof tracker? New customer, new quote, a number a customer said, a competitor mention, a pricing or ICP decision, a release, an event date, a permission granted or withdrawn.
3. For each change: the file and line it affects, the proposed new line, the source (call, message, commit) with a timestamp. Permissions go through `permission-check` for the row to add; releases go through `release-to-narrative`; quotes and numbers through `proof-capture`.
4. Flag contradictions: a fact in a context file that yesterday's evidence disputes. Do not resolve it; present both with sources.
5. Flag decisions taken in conversation that are not in `decision-log`, with the proposed entry.
6. Deliver the list for approval. Apply only the approved changes. Never write a customer permission from inference.
7. Note anything due in the next seven days from `5-current/calendar.md` that yesterday's evidence affects.

## What good looks like

- The best operator produces five lines a day that a human approves in two minutes.
- The mediocre version produces a daily summary nobody reads and the files drift for a quarter.
- Good output is a context file set where no file passes its review date.

## Rules

- MUST read full transcripts, never AI summaries, when a fact comes from a call.
- MUST cite the source and timestamp for every proposed change.
- NEVER write a change to a context file or the tracker without approval.
- NEVER infer a permission.
