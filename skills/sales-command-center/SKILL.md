---
name: sales-command-center
description: Build the one page a salesperson works from: the sales process in order with every script, asset, pricing range, template and link embedded at the step where it is used, plus the testimonial and case study request process. Use when a new salesperson is starting, when sales assets are scattered across drives and chats, when the founder is the only person who knows where things are, or when someone says "sales playbook", "onboard our salesperson", "where is the deck", "make it self-serve", "sales command center", "one place for everything sales", or "we keep rebuilding the same proposal". Works on its own with whatever assets exist.
title: Sales command center
collection: sales-enablement
type: play
playbook: 7
stage: build
---

# Sales command center

Goal: a salesperson, on day one, opens one page and can run the whole process without asking where anything is. Finding-tool time goes to zero. Every asset lives at the step where it is used. Missing assets are visible as gaps, with an owner, instead of being discovered on a live call.

## Before you start

This skill works on its own. If the person has their own marketing brain folder, read the offers, positioning, messaging and any sales playbook files. If they do not have one, ask for the folder or drive where sales material lives, the CRM they use, and who sells today. Then ask for the sales process as they would explain it to a new hire, in their own words, in five minutes. Record it if you can.

Collect every existing asset before building the page: deck, one-pagers, case studies, proposal template, pricing sheet, email templates, call scripts, demo environment links, contract template, FAQ, competitor notes. Do not rewrite them in this skill; link them. Rewriting is a separate job and goes on the gap list.

Tools this skill uses when the person has them. None are required; a single Google Doc is the usual form.

| Step | Tool | What for |
| --- | --- | --- |
| The page itself | Google Docs, Notion, or a page in the CRM | One page with live links; a doc the team already opens daily is best |
| Assets | Google Drive or SharePoint | Where the linked files live; links go to the file, not the folder |
| CRM | HubSpot or Pipedrive | Pipeline stages match the steps on the page; templates and sequences live in the CRM where possible |
| Booking and proposals | HubSpot meetings or Calendly; a proposal or e-signature tool if they have one | The links a rep sends at each step |
| Testimonials | Email, a short Google Form, or a recorded call | The approval loop for proof |

## Steps

1. Write the process as steps. Usually six to eight: lead comes in or is found, qualify, discovery call, demo, proposal, negotiation and close, handoff to delivery, review at 30 days. Each step gets: what has to be true to enter it, what the salesperson does, what they send, and what moves it to the next step. Match these to the CRM pipeline stages exactly; if they do not match, fix the stages (that is `crm-setup`) or the steps.

2. Place every asset at its step. Under each step, the links: the script, the template, the deck, the pricing range, the proposal template, the contract, the booking link, the demo environment. One line of context per link: what it is and when to use it. If an asset is used at two steps, link it twice.

3. Add the pricing ranges. The salesperson needs to answer "what does it cost" without a call to the founder. Put the offer, the sizing measure, the tier prices, the from-price for each tier, the allowed discounts with their names and reasons, and the number above which the founder gets involved. If the company will not publish exact prices internally, put the ranges and the rule.

4. Add the objection answers. The top eight to twelve objections with the two-sentence answer and the proof to point to, from the positioning doc if it exists, from the founder if not. Place them at the discovery and demo steps.

5. Add the competitor notes. One short block per competitor the company actually meets in deals: what they say about themselves, where they win, where the company wins, and the one question to ask a prospect who is considering them.

6. Add the rules. Response time on a new lead (same business day at most). Notes in the CRM after every call. Next step and date on every open deal. What is never promised (custom work, discounts without a name, timelines delivery has not confirmed). Who to ask for what.

7. Build the gap list. Every step where something is missing or out of date gets a row: asset, step, owner, due date. This list is the next month of enablement work. Do not hide gaps by linking an old deck and hoping.

8. Build the testimonial and case study process. Two parts:
   - Testimonial: when a customer says something good on a call or in an email, the salesperson drafts the testimonial in the customer's words (two to four sentences) and sends it with one question: "Would you be comfortable with us using this?" A yes-no question gets answered; a request to write something does not. Approved quotes go into a proof file with the customer's name, title, company and the date approved.
   - Case study: the trigger (a measurable result, usually at the 90-day review), the five questions to ask the customer, the one-page structure (situation, what they did, result in numbers, quote), and the approval step before publishing. Target one per quarter.

9. Write the first-week plan for a new salesperson. Day one: read the page, watch two recorded calls, set up the CRM views. Days two to five: shadow every call, practise the discovery script, send the first ten outbound messages from the template. Weeks two to four: run discovery solo with a review after each. Weeks five to eight: run demos with the founder watching. Weeks nine to twelve: run negotiations with pricing authority inside the ranges. Adjust to the company's cycle, but write it down.

10. Test the page. Give it to someone who has never sold this product and ask them to walk through a deal using only the page. Every question they ask is a gap. Fix those, then publish.

## Rules

- One page. If it needs a table of contents, it is too long; move detail into linked files.
- Link, do not copy. Copied content goes stale; linked content stays current where it is edited.
- Gaps are listed, not hidden. A missing one-pager with an owner is better than an old one presented as current.
- The CRM stages and the page steps are the same words.
- Prices are on the page. A salesperson who cannot quote cannot sell.
- The page has an owner and a monthly review date.

## Output

Return the command center page (process steps with embedded links and context), the pricing block, the objection block, the competitor block, the rules block, the gap list with owners and dates, the testimonial and case study process, and the first-week plan.

If the person has their own marketing brain folder, save to it:
- `4-playbooks/` as `sales-process.md`: the command center page
- `4-playbooks/` as `proof.md`: the testimonial and case study process and the approved proof file
- `5-current/priorities.md`: the gap list
- `5-current/decisions-log.md`: the date the page went live and its owner

If they do not have one, publish the page wherever the sales team already looks every day. Do not set up a brain unless they ask.

Next: `crm-setup` aligns the stages and builds the templates in the CRM. `discovery-and-demo` writes the scripts linked here if they do not exist. `hire-and-ramp` uses the first-week plan.
