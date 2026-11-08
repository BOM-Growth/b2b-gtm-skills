---
name: seo-audit
title: Search audit
description: |
  Use this skill for organic search: "SEO audit", "why did organic drop", "what should
  we write for search", "the site's technical health", "keyword gaps", "the blog isn't
  ranking". Produces the audit (technical issues ranked, ranked keywords, content gaps
  against competitors, the keyword set to track) and a prioritized fix list split into
  quick wins and content to write.
collection: search-aeo-and-pr
type: play
reads: [1-context/ideal-customer.md, 1-context/personas.md, 1-context/stack.md]
related: [paid-search-pr, aeo-review, blog-edit, content-calendar, landing-page-brief]
playbook: 12
stage: distribution
---

This applies quarterly, and monthly on the keyword set. It produces organic demand on the terms buyers use, without the long bets that a short quarter cannot afford.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Confirm the search tooling in `1-context/stack.md` and the site's framework and deploy process.
2. Technical: crawl the site; rank issues by pages affected and by the pages that matter (demo, product, top articles). Index files, redirects (especially after any site move), broken links, page speed on the pages that lead to a demo request.
3. Keywords: pull ranked keywords; build the keyword set from the personas' language and the ICP's vocabulary, including competitor names and category terms. Keep the set stable for tracking.
4. Content gaps: terms competitors rank for with pages we lack; questions buyers ask with no answer on our site. Map each to a page type: comparison, glossary, how-to, customer story.
5. Prioritize: quick wins (fix a title, add internal links, repair a redirect) this month; content to write into `content-calendar` by expected demand; long structural work parked unless the quarter allows it.
6. Hand page rewrites to `blog-edit`; new pages to `landing-page-brief` or the content calendar.
7. Track monthly: ranked keywords in the set, organic demo requests from the CRM, the fix list burned down.

## What good looks like

- The best operator ranks fixes by the pages that produce demo requests, not by issue count.
- The mediocre version delivers a 200-issue audit nobody actions.
- Good output is a one-page fix list with ten items this month and a content list the calendar can absorb.

## Rules

- MUST keep the keyword set stable for tracking.
- MUST route page changes through the site's deploy process.
- NEVER start a long structural project in a quarter that needs short-cycle results unless the plan allows it.
- NEVER write content for search that fails the voice or proof rules.
