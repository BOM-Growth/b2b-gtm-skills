---
name: schedule-post
title: Schedule post
description: |
  Use this skill when approved posts need to go out: "schedule these", "post it Thursday",
  "queue next week's posts", "move the post to Friday", "is it scheduled". Produces the
  posts scheduled in the publishing tool on the calendar dates with the right account
  (company page or founder), the asset attached, and the calendar status set to scheduled.
collection: content-and-proof
type: play
reads: [5-current/calendar.md, 1-context/stack.md]
related: [content-proof, content-calendar, social-post, founder-content-rhythm]
playbook: 10
stage: distribution
---

This applies once a post is approved. It produces a queue that matches the calendar, so nothing goes out early or twice.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Load `gtm-context` and `1-context/stack.md` for the publishing tool and which accounts it holds.
2. Take approved entries from `content-calendar`. Confirm each has copy, asset, link, account and date.
3. Schedule in the tool: the right account, the date and time for the audience's working hours, the asset attached, the link checked once more.
4. Write the scheduled post's id or link back to the calendar entry and set status to scheduled.
5. Check the queue for the week: no two posts on the same account within an hour, founder posts on their days only, nothing scheduled into a dead date (a holiday, a date another announcement moved to).
6. When a date changes on the calendar, move the queued post, not just the entry.
7. After publishing, set status to published and record the post link for `weekly-marketing-update`.

## What good looks like

- The best operator treats the calendar as the source and the queue as its mirror. A post moved in one place and not the other is how things go out twice.
- The mediocre version schedules from a chat message and the calendar says "drafted" for a post that went out yesterday.
- Good output is a queue that matches the calendar row for row, with every published post linked back.

## Rules

- MUST schedule only entries with status approved.
- MUST write the scheduled link back to the calendar and update status.
- NEVER post from a personal account on the founder's behalf without their standing instruction.
- NEVER schedule a post whose link or asset is missing.
