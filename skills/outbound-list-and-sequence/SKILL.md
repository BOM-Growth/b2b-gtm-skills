---
name: outbound-list-and-sequence
description: Build a prospect list that matches the target customer, verify it, write the cold email and follow-up sequence in the company's voice, set the rules for handling replies, and hand qualified replies into the CRM. Use when a B2B company has worked its warm network and needs to reach people it does not know, when someone says "build a lead list", "find prospects", "cold email", "outbound", "sequence", "we need more pipeline", "who should we be emailing", "scrape a list", "Apollo", "Clay", or "our outbound isn't working". Works on its own; the ICP card and positioning doc make it better when they exist.
title: Outbound list and sequence
collection: first-customers-and-outbound
type: play
playbook: 9
stage: distribution
---

# Outbound list and sequence

Goal: a list of real people at companies that fit, a message they would answer, a follow-up rhythm that does not need remembering, and a rule for what happens when someone replies. Outbound works when the list is right and the message is specific. Most outbound fails on the list, not the copy.

Early stage is hand-to-hand: the first version of this is 100 to 300 contacts worked by a person, not 10,000 on automation.

## Before you start

This skill works on its own. If the person has their own marketing brain folder, read the ideal customer, positioning, messaging and outreach files. If they do not have one, ask: who exactly is the buyer (industry, size, role, geography), what problem the message is about in the buyer's words, what the one-sentence offer is, and what happens when someone says yes (a call, a demo, a trial). Those four answers are enough to start.

Check what already exists before building: lists bought or scraped and never worked, old sequences, a CRM full of contacts that were never contacted. Working an existing list is faster than building a new one.

Tools this skill uses when the person has them. None are required; a spreadsheet and a mail client work for the first hundred.

| Step | Tool | What for |
| --- | --- | --- |
| Finding companies | Apollo, Clay, LinkedIn Sales Navigator; Google Maps for local businesses; industry association directories and conference attendee lists; a PDF directory parsed into a sheet | The account list that matches the segment |
| Finding people | Apollo, Clay, LinkedIn | The right role at each company |
| Verifying | Clay or Apollo email verification; a manual check of the company website for the fit facts | Bounces under 3 percent; fit confirmed by a human where enrichment is weak |
| Sending | HubSpot sequences, Pipedrive campaigns, Apollo sequences, or a sending tool like Instantly or Lemlist for higher volume | One tool. Warm the domain. Send from a person's address |
| Replies and CRM | HubSpot or Pipedrive | Replies create or update the record; qualified replies become deals |
| LinkedIn | Done by hand, or a tool only after email works | Connection and a short note, not automation on day one |
| Tracking | Google Sheets if no sequencing tool | Sent, opened, replied, meeting, by step and by segment |

## Steps

1. Write the list spec. From the ICP card if it exists; otherwise from the four answers. Industry or category, company size by the sizing measure, geography, the role titles (three to five variants), the disqualifiers, and the one or two fit facts that need a human check (what they do, how big a certain operation is). Target size for the first run: 100 to 300 contacts.

2. Build the account list. Run the spec through the tool they have, or through the directory or map search for local segments. Export to a sheet with: company, website, location, size measure, source of the record. Add a column for the human fit check and a reason.

3. Do the fit check. Someone looks at every company website for the fit facts, fast, one line each. Mark fits, needs review, does not fit. Drop does not fit. This is the step that makes the list work and the step most people skip.

4. Find and verify the people. One to three people per account in the target roles; the champion first, the economic buyer second. Verify emails; drop anything unverified. Capture a personalisation fact per person where it is cheap: a recent post, a job change, a project on their site, the city.

5. Segment the list. By the one dimension that changes the message most: industry sub-type, size tier, or trigger. Two or three segments at most for the first run. Each gets its own version of the first email.

6. Write the sequence. Four to five touches over three weeks:
   - Email 1 (day 1): one observation about them, one line on the problem in their words, one line on what the company does for companies like theirs, one proof point, one easy question. Under 90 words. No links in the first email. Subject line is plain and short, three to five words, not a pitch.
   - Email 2 (day 4): reply to the first, one new angle: a customer story in two lines or a different cost of the problem.
   - LinkedIn touch (day 6): view the profile; connect with a one-line note that does not pitch.
   - Email 3 (day 10): the direct ask: "worth a 20-minute call to see if this applies to you?" with two time options or the booking link.
   - Email 4 (day 18): the break-up: one line, no pressure, leaves the door open. Many replies come here.
   Write every touch in the company's voice from the positioning doc if it exists; otherwise ask for two emails the founder has sent that got replies and match them. No merge-field clutter, no "I hope this finds you well", no fake familiarity.

7. Set the reply rules. Every reply is read by a person and classified the same day: interested (book the call, create the deal, stop the sequence), question (answer it, stay in sequence), not now (set a follow-up date three to six months out, nurture status), referral (thank them, start a new thread with the referred person), not interested or unsubscribe (stop, mark, never again), out of office (pause, retry after the date), bounce (remove, check the domain). Write the response template for the first four.

8. Set the sending rules. One sending tool, one sender per 50 to 100 contacts per day, a warmed domain or a separate sending domain, plain text, unsubscribe honoured instantly, no sends on weekends, and compliance with the anti-spam law in the recipient's country (in Canada that means a real business reason to contact and an easy way to say stop). A person approves the sequence copy before it goes live; a person reads every reply.

9. Set the targets and the test. For a first run of 200: reply rate above 5 percent, positive reply rate above 2 percent, three to five meetings. Run it for three weeks, then read the numbers by segment and by email. Keep the segment and the email that worked, change one thing in the one that did not, run again. Do not change everything at once.

10. Hand off to the CRM. Prospects stay in the list until they reply. A positive reply creates the contact and the deal with source outbound and source detail the list name and segment. Everything else stays out of the CRM so the pipeline stays clean.

## Rules

- The list is the work. A specific list with a plain message beats a generic list with clever copy.
- A human checks fit on every account. Enrichment is a starting point, not the truth.
- Under 90 words, one question, no links, in the first email.
- Every reply gets a human answer the same day.
- One tool, one sender rhythm, no weekend sends, unsubscribe honoured instantly.
- Nothing fake: no invented observations, no claims the company cannot back, no "we worked with your competitor" unless true and approved.
- Never run LinkedIn automation on day one. Email first; LinkedIn by hand.

## Output

Return the list spec, the account list with fit check results, the contact list with verification status and personalisation facts, the segment plan, the five-touch sequence per segment, the reply rules with templates, the sending rules, the targets and the three-week test plan, and the CRM handoff rule.

If the person has their own marketing brain folder, save to it:
- `4-playbooks/outreach.md`: the list spec, the sequence, the reply and sending rules
- `1-context/ideal-customer.md`: any fit facts or disqualifiers learned from the fit check, appended
- `5-current/priorities.md`: the test targets and the review date
- `5-current/decisions-log.md`: the tool chosen and the date

If they do not have one, return the sheet and the sequence as files. Do not set up a brain unless they ask.

Next: `crm-setup` if replies have nowhere clean to land. `call-mining` once there are ten calls from this list, to sharpen the message. `event-playbook` reuses the list spec for attendee filtering.
