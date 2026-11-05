---
name: reengage-old-leads
description: Go back to closed-lost deals, stale opportunities and old leads with a real reason to talk again (new pricing, new features, a new offer, a result they asked for) and turn the ones whose situation changed into pipeline. Use when a company has a CRM full of people who said not now, when a product update or price change answers the objections that lost past deals, or when someone says "re-engage old leads", "closed lost campaign", "win back", "go back to the people who said no", "new pricing announcement", "we fixed what they asked for" or "our CRM has thousands of contacts we never talk to". Works on its own with a CRM export or a spreadsheet.
title: Re-engage old leads
collection: email-and-lifecycle
type: play
playbook: 13
stage: distribution
---

# Re-engage old leads

Goal: the people who already know the company and said not now are the cheapest pipeline there is. When something real has changed (price, product, proof, offer), tell them, specifically, in the words of their own objection, and ask one question. A good re-engagement run produces meetings in days, not months.

## Before you start

This skill works on its own. If the person has their own marketing brain folder, read the offers, messaging and ideal customer files. If they do not have one, ask: what has changed and when (the reason to write), who said no in the past and why (from the CRM lost reasons or memory), and what the first step is now.

Pull the list before writing. From the CRM or a sheet: every closed-lost deal in the last 24 months with the lost reason and the last note; every open deal with no activity in 60 days; every lead that booked or asked and never bought. If lost reasons were never recorded, the last note or email usually says why; read a sample of twenty to find the patterns.

Tools this skill uses when the person has them. None are required.

| Step | Tool | What for |
| --- | --- | --- |
| The list | HubSpot or Pipedrive export, or the spreadsheet where deals were tracked | Who, when, why lost, last contact, owner |
| The reason they left | Fathom or Granola for the old calls, the email thread | The exact objection, in their words; `call-mining` at scale |
| Sending | HubSpot or Pipedrive sequences from the original owner's address | Personal, one-to-one in tone, tracked |
| Replies | The CRM | Reopened deals with source re-engagement and the campaign name |
| Tracking | The CRM or a sheet | Sent, replied, meetings, reopened, won, by objection group |

## Steps

1. Name the change. One sentence, concrete: the price is now X, the feature they asked for ships on this date, the offer now includes Y, a customer like them got Z result. If nothing real has changed, stop; a check-in email with no news is noise and burns the list.

2. Build and group the list. Export the candidates. Drop anyone who asked not to be contacted, anyone at a company that no longer fits, and anyone contacted in the last 30 days. Group the rest by the reason they left: price, missing feature or capability, timing or no decision, chose a competitor, went quiet. Add: the person, their role, the owner, the last date, and the one line that captures their situation.

3. Match the change to the group. Each group gets a message only if the change answers its reason. Price change goes to the price group. New feature goes to the group that asked for it. A new result goes to the timing and went-quiet groups. The competitor group gets a message only if the change beats what they chose. Groups with no matching change wait for the next run.

4. Write one message per group. From the original owner, as a reply to the old thread where possible. Structure, under 100 words:
   - One line that shows you remember: the date and the thing they said ("in March you said the hold-up was X").
   - One line on what changed, specifically ("we now have X, as of this month" or "the price for a team your size is now Y").
   - One line of proof if there is one.
   - One question: "worth a 15-minute look?" or "is this still a problem for you?"
   No apology for the gap, no "just checking in", no pitch beyond the change.

5. Add one follow-up. Five to seven days later, two lines: a different proof point or a customer story, and the same question. Then stop. Two touches, not five; these people already know the company.

6. Send in batches from the owner's address. Twenty to forty a day per sender, personalised at the first line, the rest from the group template. A person reads every reply. Interested replies reopen the deal (new deal, source re-engagement, campaign name as detail, linked to the old one). Not now gets a follow-up date six months out. No gets marked and left alone.

7. Handle the reopened deals as new. Fresh discovery, short, confirming what changed on their side; do not assume the old notes still hold. Use the demo script and the current offer.

8. Report at 30 days. Sent, replied, meetings, deals reopened, won, by objection group. The group with the best meeting rate tells the company what its real objection was. Feed that to positioning and the offer.

9. Make it routine. Every product release, price change, new case study or new offer triggers a run on the matching group. Once a quarter, run the went-quiet group with the best new result regardless.

## Rules

- A real change or nothing. Never send a check-in with no news.
- Their objection, in their words, in the first line. Generic re-engagement gets ignored.
- Two touches, then stop.
- From the person they dealt with, not from marketing.
- A person reads and answers every reply the same day.
- Respect every past opt-out and every current unsubscribe.
- Reopened deals are new deals: new source, fresh discovery, linked to the old record.

## Output

Return the change statement, the grouped list with counts, the message and follow-up for each matched group, the sending plan, the reply handling rules, the 30-day report template, and the trigger list for future runs.

If the person has their own marketing brain folder, save to it:
- `4-playbooks/` as `reengagement.md`: the method, the group templates and the trigger list
- `3-strategy/messaging.md`: which objection groups responded best, dated, appended
- `5-current/decisions-log.md`: the run date, the change announced and the result

If they do not have one, return the list and the templates as files. Do not set up a brain unless they ask.

Next: `crm-setup` if lost reasons are not being recorded, so the next run is easier. `discovery-and-demo` for the reopened deals. `offer-and-pilot` if the price objection group is the largest.
