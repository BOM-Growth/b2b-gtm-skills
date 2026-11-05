---
name: crm-setup
description: Set up or clean up a B2B company's CRM so the pipeline is real, every lead lands in it with a source, nothing slips through the cracks, and the numbers can be trusted: stages, lifecycle, properties, forms and booking links, one sequencing tool, routing and follow-up rules, and the reports the weekly meeting reads. Use when a company has no CRM, uses a spreadsheet, has a CRM nobody trusts, cannot say where leads came from, or when someone says "set up HubSpot", "set up Pipedrive", "our pipeline is a mess", "leads are falling through the cracks", "clean up the CRM", "attribution", "lead routing" or "which tool should we use". Works on its own; a spreadsheet is a valid CRM at the start.
title: CRM setup
collection: crm-and-tracking
type: play
playbook: 8
stage: build
---

# CRM setup

Goal: one system of record where every lead, every conversation and every deal lives, with a source on each, a next step on each open deal, and reports that answer the weekly questions without a spreadsheet. Keep it clean: real deals only, contacts are not deals, and a lead that raised its hand is worked the same day.

## Before you start

This skill works on its own. If the person has their own marketing brain folder, read the ideal customer, offers and any sales process or website files; the stages and properties come from them. If they do not have one, ask: what CRM, if any; how leads come in today (forms, booking links, phone, email, outbound, events, referrals); who follows up and how fast; what the sales steps are in their words; and what questions they wish they could answer about the pipeline.

Do not migrate anything on day one. Read the current state first: how many contacts, how many open deals, how many have no next step, what the stages are, what properties exist and which are used. Write it down as the before picture.

Tools this skill uses when the person has them. Pick one of each; two tools doing the same job is a leak.

| Job | Options | Note |
| --- | --- | --- |
| CRM | HubSpot (Sales Hub Starter or Pro), Pipedrive, or a Google Sheet for a company under ten deals a month | Choose by what the team will actually open daily; the best CRM is the one with clean data |
| Forms and booking | HubSpot forms and meetings; Pipedrive web forms with Calendly or a Google Calendar booking link | Every form and link creates a record with a source |
| Sequences | HubSpot sequences, Pipedrive campaigns, or Apollo | One tool. Pick the one where the CRM record is updated automatically |
| Prospect data | Apollo or Clay | Prospects stay outside the CRM until they reply or are actively worked |
| Calls | CallRail or the phone system's logging; Fathom or Granola for meeting notes | Calls are leads too; log them with a source |
| Tracking | UTM parameters, Google Analytics 4, Google Tag Manager | Source on every web lead at the contact and the deal |
| Automation | Zapier or Make, or the CRM's own workflows | Routing, notifications and reminders; never for sending customer-facing messages without a person approving |
| Reports | The CRM's dashboards, or Google Sheets fed by export; Databox if they have it | The weekly numbers |

## Steps

1. Define the pipeline stages. Five to seven, each named for what the buyer has done, not what the seller did: new lead, qualified, discovery held, demo held, proposal sent, negotiating, closed won, closed lost. Write the entry rule for each stage in one line. If a sales process page exists, the stages are its steps, word for word.

2. Define what a deal is. A deal is created when a qualified buyer agrees to a discovery call or equivalent. Contacts can exist without deals. Prospects from a list do not get deals. Closed lost gets a reason from a fixed list (no budget, no fit, chose competitor, no decision, timing, other) and the competitor name if there was one.

3. Define the lifecycle and lead statuses. Contact lifecycle: subscriber, lead, marketing qualified, sales qualified, opportunity, customer, churned. Lead status on new leads: new, attempting, connected, qualified, unqualified, nurture. Every new lead starts at new with the time it arrived.

4. Define the properties that matter. Source (the fixed list: website form, booking link, inbound call, inbound email, outbound, event, referral, partner, paid search, paid social, organic), source detail (the page, the event name, the campaign), ICP tier and ICP reason, the sizing measure from the offer, decision maker yes-no, next step and next step date, lost reason. Remove or hide properties nobody fills in. Twenty good properties beat eighty empty ones.

5. Wire every entry point. List every way a lead can arrive and make each one create a record with the right source:
   - Website forms: replace email-to-inbox forms with CRM forms. Field list from the website skill or the ICP rules; keep it short.
   - Booking links: the CRM's own or a calendar tool that writes to the CRM; a qualifying question on the booking form.
   - Phone: tracked numbers or a rule that whoever answers logs the lead with the source.
   - Inbound email: a shared inbox connected to the CRM, or a rule to log it within the day.
   - Outbound replies: the sequencing tool writes the reply to the CRM and sets status to connected.
   - Events and referrals: a simple intake form or a sheet the team fills in during the week, imported with the event or referrer as source detail.
   - UTMs: a naming convention (source, medium, campaign) and the CRM capturing them on the form.

6. Set the routing and follow-up rules. Who owns a new lead by source or territory; the notification (email, Slack) the moment a lead arrives; the response target (same business day, within the hour for booked demos); the reminder if status is still new after one day; the rule that every open deal has a next step date and the view that shows the ones that do not. Automate the notifications and reminders. Never automate the customer-facing reply without a person approving it.

7. Build the sequences in one tool. Three to start: new inbound lead (three touches over a week), post-discovery follow-up (two touches), stale deal (one touch at 14 days of no activity). Templates come from the sales process if it exists; otherwise draft them short and in the company's voice. Prospecting sequences for cold lists are a separate skill and a separate list.

8. Build the views the team works from. Each salesperson: my open deals by stage, my leads with status new, my deals with no next step. The manager: all open deals, deals stuck in stage over 14 days, leads older than one day with no attempt.

9. Build the weekly report. The numbers the weekly meeting reads, in the CRM dashboard or a sheet: new leads by source, leads contacted within target, discovery calls held, demos held, proposals sent, deals won and lost with reasons, pipeline value by stage, average days in stage. If the company wants a scorecard with targets, the `scorecard-and-okrs` skill builds that on top of these.

10. Clean up and migrate. Deduplicate contacts and companies. Close out deals with no activity in 90 days as lost with the reason "no decision" and a note, or move them to a nurture status; a bloated pipeline hides the real one. Import the spreadsheet or the old tool with sources mapped to the new list. Run the entry points end to end with a test lead each. Write the one-page CRM rules for the team and walk them through it.

## Rules

- One CRM, one sequencing tool, one booking tool. Duplicates are leaks.
- Real deals only. Contacts are not deals; lists are not deals.
- Every record has a source. "Unknown" is a bug to fix, not a category to keep.
- Every open deal has a next step and a date.
- Same-day follow-up on inbound. Automate the reminder, not the reply.
- Attribution at deal level, not just contact level, or the channel numbers mean nothing.
- Change nothing in bulk without a backup export first.

## Output

Return the before picture, the stage definitions with entry rules, the deal and lifecycle rules, the property list, the entry point wiring list with sources, the routing and follow-up rules, the three sequences, the views, the weekly report definition, the cleanup and migration plan, and the one-page CRM rules for the team.

If the person has their own marketing brain folder, save to it:
- `4-playbooks/crm-setup.md`: the stage definitions, properties, entry points, routing rules and team rules
- `2-standards/terminology.md`: the source list and the stage names, so everyone uses the same words
- `5-current/decisions-log.md`: the tool choices and the date

If they do not have one, return the CRM rules as a one-page file the team keeps in the CRM itself. Do not set up a brain unless they ask.

Next: `scorecard-and-okrs` puts targets on the weekly report. `outbound-list-and-sequence` builds the prospecting list outside the CRM and the handoff into it. `homepage-rewrite` supplies the form fields if the site is being redone.
