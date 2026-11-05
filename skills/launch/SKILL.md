---
name: launch
title: Launch (playbook)
description: |
  Entry point for a marketable release: "we're launching", "plan the launch", "the new
  version", "when do we announce", "what goes out and when", "customers need to hear
  about this", "rebrand", "relaunch". Routes the plays in order: narrative, calendar,
  internal brief, customer kit, win-back, press. Keeps one hard launch date.
collection: launch
type: playbook
reads: [5-current/calendar.md, 2-standards/proof-rules.md, 1-context/personas.md]
related: [release-to-narrative, launch-calendar, launch-internal-brief, customer-launch-kit, closed-lost-winback, press-release, customer-update-email]
playbook: 18
stage: distribution
---

This applies when a release is big enough to market as an event. It produces a dated plan every team reads, and a launch that lands in one window instead of leaking out.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Run `release-to-narrative` first: what the release means, its maturity label, what may be claimed.
2. Decide if this is a launch or a product update. A launch answers a known objection, opens a segment or changes the category story. An update goes to `product-tip-series` and `customer-update-email`.
3. Run `launch-calendar`: one hard launch date, the tease and announce dates, the customer rollout window, checked against the industry dead zones in `5-current/calendar.md`.
4. Run `launch-internal-brief` before any external mention. Management first, then the company, with talking points.
5. Run `customer-launch-kit` so existing customers hear first and have something to share.
6. Line up the demand plays for the window: `closed-lost-winback`, `press-release` and `pr-brief`, `social-post` series, `nurture-email`, event tie-ins. One two-week window, all channels.
7. Set what sales and success may demo and promise, by maturity label, and how prospects who want to buy before general availability are handled.
8. After the window, run `experiment-readout` on the launch: reactivated deals, demos, press, traffic, against the targets set in step 3.

## KPIs

- Deals reactivated and demos booked in the launch window.
- Customers reached before the market (share of the base that heard first).
- Press placements and referral traffic in the window.

## What good looks like

- The best operator notices the leak before it happens: a partner newsletter, a magazine banner, a rep's cold message. The calendar exists to make the first mention deliberate.
- The mediocre version announces a date nobody committed to, then slides it, and customers find out from a third party.
- Good output is a calendar with one hard date everyone has agreed to, an internal brief that went out first, and a window where every channel said the same thing.

## Rules

- MUST have one hard launch date agreed by product, sales, success and marketing before anything external goes out.
- MUST brief the company before customers, and customers before the market.
- NEVER promise a ship date for anything not generally available.
- NEVER launch into the industry dead zone in `5-current/calendar.md`.
