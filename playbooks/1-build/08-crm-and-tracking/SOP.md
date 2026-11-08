# CRM and tracking

Status: draft
Playbook 8 of 19. Stage: Build. Usually runs after the website forms are planned, before scorecard and outbound. Every skill in it works on its own.

## What it produces

One system of record with real deals only, a source on every lead, a next step on every open deal, every entry point wired in, one sequencing tool, routing and follow-up rules, and the reports the weekly meeting reads.

## Why it matters

If the pipeline is not clean the numbers are not real, and if a lead cannot be traced to a source then no channel can be judged. Leads that sit in an inbox are the most expensive leak a company has. A spreadsheet is a fine CRM for a company closing under ten deals a month, as long as the rules hold.

## Order of operations

1. Read the current state and write the before picture.
2. Define the stages, what a deal is, the lifecycle and the properties that matter.
3. Wire every entry point: forms, booking links, phone, inbound email, outbound replies, events, referrals, UTMs.
4. Set routing, response targets and reminders; automate the reminder, never the customer-facing reply.
5. Build three sequences in one tool, the views the team works from, and the weekly report.
6. Clean up, deduplicate, close stale deals, migrate, test every entry point with a test lead.
7. Write the one-page rules and walk the team through them.

## Who is involved

The go-to-market lead designs it. Whoever sells agrees the stages and lives by the rules. One person owns the CRM. The founder agrees the response target.

## How long it takes

Two to three weeks for a first setup or a cleanup. Then a monthly hygiene check.

## Signs it needs revisiting

- Leads arrive with source unknown.
- Open deals have no next step.
- Two tools are sending sequences.
- The weekly numbers need a spreadsheet to assemble.

## Skills in this playbook

| Skill | Type | What it does |
| --- | --- | --- |
| `inbound-lifecycle` | playbook | Every hand-raise and every email the company sends to people it already knows: "a demo request came in", "triage this lead", "where did this lead come from", "attribution", "the routing form", "nurture email", "customer email", "the weekly send", "landing page for", "send me something to look at". |
| `crm-setup` | play | Set up or clean up a B2B company's CRM so the pipeline is real, every lead lands in it with a source, nothing slips through the cracks, and the numbers can be trusted: stages, lifecycle, properties, forms and booking links, one sequencing tool, routing and follow-up rules, and the reports the weekly meeting reads. |
| `funnel-definitions` | play | Whenever a number's meaning is in question: "what counts as an MQL", "define SQL", "why do sales and marketing numbers differ", "is a demo request a lead", "the stage definitions", "set up the funnel fields". |
| `lead-source-audit` | play | When the source numbers cannot be trusted: "where are leads coming from", "attribution is broken", "the source field is empty", "the form isn't tagging", "what did paid actually produce", "the CRM says direct for everything". |
| `inbound-triage` | play | On every inbound lead: "a demo request came in", "triage the inbound", "is this lead real", "who should take this", "the form submissions this week". |
| `demo-routing` | play | When a fit lead needs a rep and a slot: "route this demo", "who owns this account", "the demo didn't get booked", "the handoff to sales", "round robin", "the rep brief for tomorrow's demo". |
