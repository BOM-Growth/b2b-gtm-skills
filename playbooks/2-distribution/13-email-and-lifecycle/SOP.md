# Email and lifecycle

Status: draft
Playbook 13 of 19. Stage: Distribution. Usually runs after CRM and tracking, before scaling any channel. Every skill in it works on its own.

## What it produces

Leads nurtured until they are ready, customers onboarded to value fast, old leads re-engaged with a real reason, and churn caught early. One sequencing tool, a person approving every message.

## Why it matters

Most of the people the company has already talked to are not ready today. A written sequence for each situation means they are followed up the same way every time, and the ones whose situation changes come back. Re-engaging closed-lost deals when something real has changed is the cheapest pipeline there is.

## Order of operations

1. Define the situations: new inbound lead, post-discovery, stale deal, not now, new customer, at risk, closed lost.
2. Write one short sequence per situation in the company's voice, in the one tool the CRM uses.
3. Set the triggers: a stage change, a date, a product or price change.
4. For re-engagement, group old leads by why they left and write to each group only when the change answers it.
5. A person reads every reply the same day; positive replies become deals.
6. Review monthly: replies, meetings and reopened deals by sequence.

## Who is involved

The go-to-market lead writes the sequences. Whoever sells owns the replies and the re-engagement runs. Whoever delivers writes the onboarding emails.

## How long it takes

The core sequences in a week. A re-engagement run in a week to build and a month to read.

## Signs it needs revisiting

- A product or price change shipped and nobody told past leads.
- Sequences in two tools.
- Replies waiting more than a day.

## Skills in this playbook

| Skill | Type | What it does |
| --- | --- | --- |
| `reengage-old-leads` | play | Go back to closed-lost deals, stale opportunities and old leads with a real reason to talk again (new pricing, new features, a new offer, a result they asked for) and turn the ones whose situation changed into pipeline. |
| `closed-lost-winback` | play | When something has changed that answers a past objection: a release, a pricing change, a new package, a segment opened. |
| `nurture-email` | play | For the emails to leads who are not ready: "the nurture sequence", "what do we send the leads who didn't book", "the post-webinar sequence", "the event leads that went cold", "a drip for", "re-engage the old leads". |
| `customer-update-email` | play | For email to existing customers: "the monthly customer update", "the release notes email", "tell customers about", "the newsletter", "the product update email for". |
