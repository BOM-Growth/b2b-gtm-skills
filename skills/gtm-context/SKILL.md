---
name: gtm-context
title: GTM context
description: |
  Use when a question or task touches the company's go-to-market facts: who we sell to,
  what we claim, how we sound, which tool holds which record, what the funnel stages mean,
  what the calendar allows. Produces the answer with the file it came from cited, or a
  plain "the context does not say" when it does not. Triggers on "what's our ICP", "can we
  say", "who owns", "where does that live", "is that still true". Every other skill in this
  repo reads the context this way before it starts.
collection: marketing-brain
type: foundation
reads: [1-context/ideal-customer.md, 1-context/personas.md, 3-strategy/funnel.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md, 1-context/stack.md, 5-current/calendar.md]
related: [marketing-brain, permission-check, decision-log]
playbook: 2
stage: foundation
---

This applies whenever a skill needs a fact about the company. It produces cited facts or an honest gap, never a guess.

## Before you start

This skill works on its own. If the person has their own marketing brain (the folder from the `marketing-brain` skill, or any folder of context files they point you to), read it. If they do not have one, do not look for one and do not set one up: answer from what they tell you in the conversation, say plainly what is missing, and offer the `marketing-brain` skill once.

## The play

1. If a marketing brain exists, read `README.md`, then `1-context/`, `2-standards/` and `3-strategy/`. Treat `5-current/` as the latest status. If the company keeps a fuller knowledge base (a wiki, a repo), read its index too and treat it as the source the brain summarises.
2. Find the fact in the files. Quote the value and name the file and section it came from.
3. Check freshness. A file carries a status line or a last-reviewed date; say when a fact is past it or marked draft.
4. If the fact is not there, say so in one line and name who could settle it. Do not fill the gap from general knowledge.
5. If two files disagree, the knowledge base wins over a skill's own copy, and the newer dated decision wins over the older. Flag the disagreement; do not pick silently.
6. Hand the fact to the skill that needs it with the citation attached so the output can carry it.

## What good looks like

- The best operator notices that most wrong marketing output is built on a stale fact, not a bad sentence: an old product name, a retired claim, a persona from two ICPs ago. Checking the file first is cheaper than rewriting the piece.
- The mediocre version answers from memory because it sounds right, then cites nothing. The output reads fine and contradicts the current decision.
- Good output names the file for every fact, says "not in context" where that is true, and surfaces a conflict instead of resolving it quietly.

## Rules

- MUST cite the file and section for every fact used when a brain exists.
- MUST say when a file is a draft or past its stale date.
- NEVER invent a fact the context does not hold, including a safer-sounding version of a claim.
- NEVER assume a marketing brain exists, and never set one up unless asked.
