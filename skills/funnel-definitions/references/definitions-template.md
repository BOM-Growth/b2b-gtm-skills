# Funnel definitions template

Fill one row per stage. A rule must be testable from the CRM record alone.

| Stage | Entry rule | Exit forward | Exit out | Owner | CRM field = value | SLA to next stage |
|---|---|---|---|---|---|---|
| Visit | Session on the site or a tracked page | Form or booking | none | Marketing | analytics only | n/a |
| Lead | Identified person at a company (form, scan, referral, reply) | Fit and intent confirmed | Not fit, logged reason | Marketing | lifecycle = lead | same business day to triage |
| Qualified lead | Passes the ICP gates and shows intent | Demo requested or booked | No intent after nurture exit | Marketing | lifecycle = qualified | per source SLA |
| Demo request | Asked for a demo (form, booking, reply, rep note) | Demo held | No-show after one reschedule | Marketing to sales | lifecycle = demo_request | one business day to booked |
| Demo held | Demo meeting occurred | Opportunity created | Not a fit, logged reason | Sales | lifecycle = demo_held | five business days to opportunity decision |
| Opportunity | Rep confirms budget, authority, need and a timeline | Closed won | Closed lost, reason required | Sales | deal stage per pipeline | per pipeline |

## Source mapping

| Source | Enters at | Qualification step | Source field value |
|---|---|---|---|
| Web demo form | Demo request | ICP fit check | web_demo |
| Web other form | Lead | Triage | web_form |
| Event scan | Lead | Fit and intent from the scan note | event_<name> |
| Referral | Lead | Referrer's note | referral |
| Partner handoff | Qualified lead | Partner's note | partner_<name> |
| Outbound reply | Lead or demo request by intent | Reply handling | outbound_<cohort> |
| Paid click to demo page | Demo request | ICP fit check | paid_<channel> |

## Reconciliation record

| Date | Dispute | Records in question | Rule applied | Outcome | Decision-log id |
|---|---|---|---|---|---|
