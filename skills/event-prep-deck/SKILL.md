---
name: event-prep-deck
title: Event prep deck
description: |
  Use this skill in the final prep before a show: "team prep deck", "prep call for
  the show", "talk tracks", "what do we say at the booth", "booth rules", "who's on
  which shift". Produces the team prep deck from the fixed outline with every fact
  pulled from context, plus the talk-track drill agenda. See references/deck-outline.md.
collection: events
type: play
reads: [5-current/calendar.md, 1-context/ideal-customer.md, 1-context/personas.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md, 1-context/stack.md]
related: [events, event-plan, event-outreach, event-lead-ingest, permission-check]
playbook: 14
stage: distribution
---

This applies before the prep call. It produces a deck that never needs a compliance pass afterwards, because every fact came from context.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Pull the event row from the events system of record: logistics, team, shifts, goals set by the sales lead.
2. Build the deck from `references/deck-outline.md`, section by section. Every fact comes from a context file or the system of record; cite it in the notes.
3. Write the qualifying questions from `1-context/ideal-customer.md` in the words a booth person would say, and the polite exit for out-of-ICP visitors (still scan, ask for referrals).
4. Write the conduct rules: two in the booth at all times, huddles before and after each day, never guess (note the question, follow up), send pricing questions to sales, turn a trial request into a booked call, say clearly when a feature is not released yet, do not criticize competitors, agree the dress code.
5. Pull cleared company claims and approved customers through `permission-check`. Nothing from the not-cleared list enters the deck or the booth.
6. Add the demo flow: show what customers can use today, say so when something is a preview, and list what is not shown.
7. Add the competitor section from context: the kinds of competition at a show and the quick compare-and-pivot for each direct competitor likely present.
8. Set the drill: a short rapid-fire talk-track run with the whole on-site team, and a refresher at the kickoff huddle the night before.

## What good looks like

- The best operator writes the deck for the newest person on the team, so anyone can qualify, answer or exit a conversation without inventing anything.
- The mediocre version is a logistics deck with a product slide that says "latest features" and no rules, so three people say three different things about pricing.
- Good output is a deck the sales lead can drill the team on in one short session, with no claim in it that marketing would have to walk back.

## Rules

- MUST pull every claim, customer and figure from context through `permission-check`.
- MUST mark every feature that is not released yet as a preview.
- NEVER include pricing figures, unapproved customer names or superlatives not on the cleared list.
- NEVER skip the talk-track drill.
