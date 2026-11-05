---
name: paid-weekly-report
title: Paid weekly report
description: |
  Use this skill every week for paid channels: "spend by channel", "how are the ads
  doing", "cost per demo", "what's the paid update", "are the ads working yet".
  Produces one table: spend, demo requests, cost per demo request, by channel, on the
  one conversion definition, with last week beside it and two lines on what changes
  next week.
collection: paid-channels
type: play
reads: [3-strategy/funnel.md, 1-context/stack.md]
related: [paid-search-pr, google-ads, linkedin-ads, weekly-marketing-update, funnel-definitions]
playbook: 11
stage: distribution
---

This applies weekly, before the marketing update. It produces the one paid table every stakeholder can trust.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). The conversion is the demo request; every channel is counted on it.
2. Pull spend by channel from the ad platforms or the reporting tool in `1-context/stack.md`. Pull demo requests by first-touch source from the CRM, not from the platforms.
3. Compute cost per demo request by channel. Where attribution is known to be broken for a channel, say so on the row rather than report a number.
4. Add coverage lines for the channels whose job is reach: share of the TAM reached, engaged accounts, from `linkedin-ads`.
5. Compare to the prior week and the four-week average. Note any change in the account (a pause, a budget move, a new campaign) that explains a swing.
6. Write two lines: what changes next week and why, typed as cut, scale, build or test.
7. Hand the table to `weekly-marketing-update`. Keep the history so the monthly and quarterly reads come from the same numbers.

## What good looks like

- The best operator takes demo requests from the CRM, not from the ad platforms, so the number means the same thing every week.
- The mediocre version pastes platform dashboards side by side and compares conversions that count different things.
- Good output is a table that has not changed shape in a quarter, with every swing explained.

## Rules

- MUST count demo requests from the CRM on the `3-strategy/funnel.md` definition.
- MUST flag broken attribution on the row instead of estimating.
- NEVER compare platform-reported conversions across channels.
- NEVER report closed won here.
