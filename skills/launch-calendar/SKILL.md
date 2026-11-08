---
name: launch-calendar
title: Launch calendar
description: |
  Use this skill when a release will be marketed and nobody has landed the date: "when
  are we launching", "plan the launch dates", "tease, announce, launch", "what goes out
  when", "news got out early", "customers need to hear first". Produces one hard
  launch date, the tease and announce dates, the customer rollout window, the channel
  plan for the launch window, and the owners, checked against the slow periods.
collection: launch
type: play
reads: [5-current/calendar.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [launch, release-to-narrative, launch-internal-brief, customer-launch-kit, press-release]
playbook: 18
stage: distribution
---

This applies once a release is confirmed as a launch. It produces the dates everyone can plan against and the rule for what leaves the building when.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Read the launch rhythm offsets and the slow periods.
2. Get the engineering and product dates: when it is demoable, when customers can opt in, when it is generally available. Confirm with the product owner; do not infer.
3. Set one hard launch date. It must sit outside the slow periods and after the date the product can be demoed to new prospects. Everything else is offset from it.
4. Set the tease date (two weeks before, or per `5-current/calendar.md`), the internal brief date (before any external mention), the announce date, the full launch date and the customer rollout window.
5. Build the channel plan for the launch window: founder and company posts, press release, nurture send, customer kit, closed-lost win-back, event tie-ins, site changes. One two-week window, same message everywhere.
6. Name every third party that could mention it early (a publication, a partner, a reseller) and set their date deliberately, or hold them.
7. Set the rules for sales and success during the window: what may be demoed, what may be promised, how a prospect who wants to buy before general availability is handled.
8. Publish the calendar in the content calendar and log the date with `decision-log`.

## What good looks like

- The best operator asks "what is the first external mention and who controls it" before setting the date. Leaks come from third parties with their own schedules.
- The mediocre version picks the date product hopes for, announces it, and slides it twice.
- Good output is a one-page calendar where every row has a date, an owner and a channel, and the hard date is agreed in writing by product, sales, success and marketing.

## Rules

- MUST have one hard launch date agreed by product, sales, success and marketing.
- MUST schedule the internal brief before any external mention.
- NEVER set the launch inside a slow period listed in `5-current/calendar.md`.
- NEVER announce a general availability date that engineering has not committed to.
