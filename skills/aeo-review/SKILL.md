---
name: aeo-review
title: AI answer visibility review
description: |
  Use this skill to check how the company shows up where buyers now ask: "are we in
  the AI answers", "what does the assistant say about us", "our competitor shows up and
  we don't", "AEO", "the prompts buyers ask", "llms.txt". Produces the prompt set buyers
  use, our presence and citations on each versus competitors, the pages that earn
  citations, and the next fixes for the content calendar.
collection: search-aeo-and-pr
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [paid-search-pr, seo-audit, blog-edit, content-calendar, landing-page-brief, weekly-marketing-update]
playbook: 12
stage: distribution
---

This applies monthly. It produces a read on the channel that is replacing search for buyers who research before they talk to a vendor.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Build the prompt set from the personas: the questions a buyer asks an assistant at each stage (what tools exist, how they compare, is X worth it, who uses X for Y). Twenty to forty prompts; keep them stable month to month.
2. Run the prompts through the visibility tool in `1-context/stack.md` or by hand. Record for each: are we mentioned, cited, or absent; which competitors appear; which of our pages are cited.
3. Check the plumbing once a quarter: the AI crawler index file, the search engine submission, structured data on the key pages, the pages' answer-first structure.
4. Find the pages earning citations and the prompts where competitors are cited and we are not. Map each gap to a page to write or rewrite: an answer-first opening, a comparison page, a glossary entry, a customer story on the specific job.
5. Hand the page list to `content-calendar` with the prompt each page targets; route rewrites through `blog-edit`.
6. Trend month over month: share of prompts where we appear, cited pages, competitor share. Report in `weekly-marketing-update` monthly.

## What good looks like

- The best operator keeps the prompt set fixed and watches the trend. Changing the prompts every month makes the number meaningless.
- The mediocre version writes "AI SEO" content about AI instead of answering the buyer's actual questions.
- Good output is a short list of prompts where we gained or lost presence, and the one page that would change each.

## Rules

- MUST keep the prompt set stable across months.
- MUST route every claim on a rewritten page through `permission-check`.
- NEVER treat an assistant's answer as a fact about the company; it is evidence of visibility only.
- NEVER cite a competitor's claim as true in comparison content.
