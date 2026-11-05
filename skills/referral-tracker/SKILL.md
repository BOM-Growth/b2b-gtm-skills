---
name: referral-tracker
title: Referral tracker
description: |
  Use this skill whenever a referral arrives or someone asks about the program's results:
  "who referred this", "how many referrals", "do we owe anyone", "pipeline from referral",
  "pay out the reward". Produces the tracker row (referrer, referred, date, demo held,
  deal, payout status), the running totals, and the payouts due.
collection: referral-and-partners
type: play
reads: [3-strategy/funnel.md, 1-context/stack.md]
related: [referral-partners, referral-campaign, inbound-triage, weekly-marketing-update]
playbook: 19
stage: distribution
---

This applies from the first intro onward. It produces the record that lets the company pay what it promised and report what the program did.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). The tracker lives in the CRM (a referral source, a referrer field) or a shared sheet named in `1-context/stack.md`; pick one and keep it.
2. On every intro: record referrer, referred person and company, date, how it arrived (one-click email, form, verbal through a rep). Source = referral on the lead.
3. Run `inbound-triage` on the referred lead the same day; write the tier back to the row.
4. Update the row as the lead moves: demo held, deal created, closed won or lost. The stage definitions in `3-strategy/funnel.md` decide when a payout milestone is met.
5. List payouts due with the referrer, the milestone, the amount from the terms, and the status (due, approved, paid). Hand to finance with the referred account named.
6. Report in `weekly-marketing-update`: intros, demos, deals and pipeline from referral, and referrers who have brought more than one.
7. Thank referrers at each milestone through the relationship owner, not an automated message.

## What good looks like

- The best operator pays visibly and fast. The second referral from the same person is the signal the program works.
- The mediocre version loses the referrer's name when the lead is converted and cannot say who is owed what.
- Good output is a row per referral that finance and success can both read, and a monthly number for referred pipeline.

## Rules

- MUST record the referrer on the lead before anything else happens to it.
- MUST use the stage definitions in `3-strategy/funnel.md` for payout milestones.
- NEVER pay or promise outside the stated terms.
- NEVER drop a referred lead that is out of ICP without telling the referrer.
