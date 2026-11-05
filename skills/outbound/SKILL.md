---
name: outbound
title: Outbound (playbook)
description: |
  Entry point for prospecting and re-engagement with sales: "next cohort", "who do we
  email this week", "re-engage closed lost", "pricing campaign", "win-back", "sequence
  copy", "signal-based outbound", "website visitors", "new followers", "we have the
  signal, we just have to execute". Routes cohort definition, copy, signals and reply
  handling, one cohort a week.
collection: first-customers-and-outbound
type: playbook
reads: [1-context/ideal-customer.md, 1-context/personas.md, 3-strategy/funnel.md, 1-context/stack.md]
related: [outbound-cohort, outbound-sequence-copy, signal-to-outreach, reply-handling, closed-lost-winback, build-target-list]
playbook: 9
stage: distribution
---

This applies every week there is a sales team to feed. It produces one cohort, one sequence and one owner per week, and keeps marketing's role clear: messaging, lists and signals in; demos out.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm who runs outbound (usually sales ops) and who marketing hands lists and copy to.
2. Run `outbound-cohort` to pick this week's cohort from the taxonomy: cold by persona ladder, warm (old prospects), closed-lost by reason, event follow-up, signal-driven. Cheap-to-fail cohorts first.
3. Run `build-target-list` for the cohort from the TAM and the gates; dedupe against active pipeline and recent sends.
4. Run `outbound-sequence-copy` for the cohort and persona, from the context messaging and objections, in the agreed sequence shape.
5. Run `signal-to-outreach` continuously alongside: followers, site visitors, call mentions become their own small cohorts.
6. Hand the cohort and copy to the sequence owner with the send date, the sender, the calendar it books into, and the overflow rule (rotate to a second calendar if one fills).
7. Run `reply-handling` on replies; every booked demo becomes a deal at the first pipeline stage.
8. Weekly: reply rate and demos by cohort back into `weekly-marketing-update`. A cohort that flops is replaced, not repeated.

## KPIs

- Reply rate and demos booked per cohort.
- Share of booked demos inside the ICP gates.
- Time from cohort decision to first send (target: the same week).

## What good looks like

- The best operator sequences cohorts by how cheap they are to fail: small accounts and users first, executives last, and reads each week's result before the next cohort goes.
- The mediocre version blasts the whole TAM with one message, burns the list, and cannot tell which angle worked.
- Good output is a weekly rhythm where the cohort is decided Monday, copy is approved the same day, and the demos it books are visible in the pipeline by Friday.

## Rules

- MUST dedupe every cohort against active pipeline and sends in the last 30 days.
- MUST give each cohort its own angle; a closed-lost account hears about what changed, not the cold pitch.
- NEVER send without the permission check on every proof point in the copy.
- NEVER let marketing book or run the demos; route to the sales calendar.
