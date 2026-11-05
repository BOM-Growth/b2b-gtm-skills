---
name: google-ads
title: Paid search
description: |
  Use this skill to run or audit paid search for B2B: "the search campaigns", "search
  term report", "negatives", "competitor ad group", "quality score", "the landing page
  for ads", "CPCs are up", "shift budget between campaigns", "take the account back
  from the agency". Produces the weekly audit (search terms classified by intent,
  negatives, bids, budget shifts), the account structure, and the change log, on the
  one conversion definition. Pairs with the generic paid-search skills on gtmskills.com.
collection: paid-channels
type: play
reads: [3-strategy/funnel.md, 1-context/ideal-customer.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [paid-search-pr, ad-copy, paid-weekly-report, landing-page-brief, aeo-review]
playbook: 11
stage: distribution
---

This applies weekly. It produces an account that captures the demand that exists without paying for the demand that does not.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). The conversion is the demo request as defined there; nothing else is optimized for.
2. Structure: brand, competitor, category and problem campaigns, each with its own intent and budget. Brand stays live at all times; it is the cheapest demand there is.
3. Weekly search term audit: classify every term by intent (ready to buy, comparing, researching, wrong). Add negatives for wrong and researching terms that spend without converting. Promote converting terms to exact match.
4. Competitor terms: a comparison page, not the home page; honest comparison, no disparagement, names cleared under the naming rules.
5. Landing page: the page the ads land on exists for ads only, matches the ad's promise, carries the tracking the site requires, and has one action. Changes go through `landing-page-brief`.
6. Bids and budget: separate rank pressure from budget pressure before changing either. A campaign capped by budget with a good cost per demo gets budget from one past its efficient point.
7. Read the change history. A channel that fell off in one quarter with no structural change usually has an operator or competition cause; find it before cutting spend.
8. Log every change with the reason. Report in `paid-weekly-report`.

## What good looks like

- The best operator reads the search term report before the dashboard. The terms say what the market is asking for this week.
- The mediocre version watches cost per click and reallocates on platform conversions that count page visits.
- Good output is an account where every campaign has a stated intent, brand is never paused, and the weekly change log explains every move.

## Rules

- MUST optimize for the conversion in `3-strategy/funnel.md` only.
- MUST keep brand search live.
- NEVER compare this channel to paid social on platform-reported conversions.
- NEVER run a claim or customer name in an ad that failed `permission-check`.
