---
name: event-scorecard
title: Event scorecard
description: |
  Use this skill when deciding whether to exhibit at, attend, sponsor or speak at a show:
  "should we do this show", "is it worth it", "they want us to sponsor", "which shows next
  year", "we found out about an event next month". Produces a scored verdict (exhibit,
  attend, speak, pass) with the tests that failed, the payback math and the lead-time
  check. See references/scorecard.md for the rubric.
collection: events
type: play
reads: [5-current/calendar.md, 1-context/ideal-customer.md, 1-context/stack.md]
related: [events, event-plan, association-play, speaking-proposal]
playbook: 14
stage: distribution
---

This applies before money or a calendar slot is committed. It produces a verdict a skeptic can check.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Load `gtm-context` and `5-current/calendar.md`: the lead-time minimum, the payback test and the scorecard thresholds.
2. Check lead time first. Under the minimum, the verdict is pass, regardless of the rest. The next year's show goes on the calendar with its speaking deadline.
3. Gather the show facts: attendance and who attends (buyer roles or vendors), sub-vertical depth, our past results there, speaking and sponsorship options and deadlines, parallel programming that pulls people off the floor, partner presence, competitor presence.
4. Score the tests in `references/scorecard.md`. Fails at or above the threshold means pass on the show.
5. Run the payback math: fully loaded cost (booth, travel, people days, collateral, sponsorship) against the ARR the show must produce within the horizon to hit the ratio. State the number of deals that implies at the average deal size.
6. Decide the format: exhibit, attend without a booth, speak only, host a dinner alongside, or pass. Attending without a booth is often the right answer for a show that passes the audience test and fails the economics.
7. Write the verdict with the failed tests and the payback target, and log it with `decision-log`. Add the show and its speaking deadline to the calendar either way.

## What good looks like

- The best operator asks who walks the floor on the last afternoon. A show full of vendors and media is a show where the booth sells to no one.
- The mediocre version goes because competitors go, or because the organizer offered a discount, and cannot say afterwards what it should have produced.
- Good output is a one-page verdict with a payback number the sales lead agreed to before the deposit was paid.

## Rules

- MUST pass on any show inside the minimum lead time.
- MUST state the payback target in ARR and deals before committing.
- NEVER score on brand presence alone; shows are pipeline events.
- NEVER skip the speaking deadline; apply the day the prior show ends.
