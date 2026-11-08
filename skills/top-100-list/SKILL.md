---
name: top-100-list
description: Build a list of 100 people who might know a buyer and draft the message to send them. Use when a business has few or no customers yet and needs its first sales conversations.
title: Top 100 list
collection: first-customers-and-outbound
type: play
playbook: 9
stage: distribution
---

# Top 100 list

Goal: the person's first customers come from people they already know, or people those people know. This skill builds the list and makes the first 20 messages easy to send.

Nobody is finding them yet, so they go find the customer. At this stage it is sales, not marketing.

## Before you start

This skill works on its own. If the person has their own marketing brain, read the ideal customer file first. If they do not, work from the one-sentence customer description in step 2. Tools: their phone contacts, LinkedIn connections and a Google Sheet for the tracker; nothing else is needed.

## Steps

1. Ask for their one-liner. If they do not have one, run the `positioning-one-liner` skill first, or ask them to describe what they do and for whom in one sentence and work with that.
2. Ask who their customer is in one sentence. Write it down and refer to it throughout.
3. Build the list in rounds. For each round, ask them to name everyone they can think of, then move on. Do not let them judge whether someone is "worth it".
 - Round 1: people who ARE the customer. Past clients, people who asked about this before, anyone who fits.
 - Round 2: people who talk to the customer every day. Suppliers, accountants, lawyers, consultants, trade associations, community groups.
 - Round 3: former coworkers and bosses.
 - Round 4: friends, family, neighbours, people from school, sports, church, volunteering.
 - Round 5: everyone else in their phone, LinkedIn connections, Instagram follows. Suggest they scroll their contacts while answering.
4. Stop at 100 or when they run dry. Fewer than 60 is fine to start.
5. Score each person 1 to 3: 3 = likely knows a buyer or is one, 2 = might, 1 = long shot. Sort by score.
6. Draft the ask. One message, under 50 words, adjusted lightly per person. Structure:
 - One line of real context (how you know them, or what you last talked about)
 - The one-liner
 - The ask: "Do you know anyone who [problem the customer has]?"
 - Nothing else. No link, no pitch, no "let me know if you'd like to hop on a call".
7. Write a tracker as a table: Name, How I know them, Score, Date sent, Replied, Intro made, Next step. Offer it as a CSV or a spreadsheet.
8. Set the target: 20 messages sent this week, every reply answered within a day.

## Rules

- Never generate names. The list comes from the person's own memory and contacts.
- Keep the ask about referrals, not about selling to the person directly. "Do you know anyone" is easier to answer than "do you want to buy".
- When they say outreach feels uncomfortable, agree that it does, and say it works anyway. Do not soften the target.

## Output

Return the sorted list, the message template with two or three personalized examples, and the tracker. Suggest saving the customer description to `marketing-brain/1-context/ideal-customer.md` and the message template to `marketing-brain/4-playbooks/outreach.md` if they have a marketing brain folder.
