---
name: landing-page-brief
title: Landing page brief
description: |
  Use this skill before any page is built or changed: "a landing page for", "the demo
  page isn't converting", "a page for the campaign", "the comparison page", "the
  pricing page copy", "rewrite the home page". Produces the brief: the page's one job,
  the audience and source, the message hierarchy, the proof blocks with cleared
  sources, the form and tracking requirements, the copy draft, and the acceptance
  checks.
collection: website-and-conversion
type: play
reads: [1-context/personas.md, 2-standards/proof-rules.md, 2-standards/brand-voice.md, 3-strategy/funnel.md, 1-context/stack.md]
related: [inbound-lifecycle, google-ads, seo-audit, aeo-review, leave-behind-page, graphics-check, permission-check]
playbook: 6
stage: build
---

This applies before building any page. It produces a page with one job, built once, with the tracking that makes it reportable.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). State the page's one job (demo request, event registration, download, comparison) and the one source it serves (ads, email, event, organic). A page with two jobs gets two pages.
2. Audience: the persona and tier, where they come from, what they already know. The headline answers the question they arrived with.
3. Message hierarchy: headline (the outcome in the customer's words), subhead (how, in one line), three proof blocks (a cleared number, a cleared customer, a product view), the ask. Each proof block cites its tracker row through `permission-check`.
4. Form and tracking: the fields the triage needs and no more; the source parameters the page must carry into the CRM (from `lead-source-audit`); the events analytics must fire; the thank-you path.
5. Copy draft in `brand-voice`; a comparison page follows the naming rules and the honest-comparison rule.
6. Visuals: real product screenshots, cleared logos, no clipped frames; check through `graphics-check`.
7. Acceptance checks: the form writes the right source, the events fire, the page passes the voice and proof rules, mobile renders, speed on the demo path. Route to the site's deploy process.
8. After launch: read it on demo requests from that source, not on page views.

## What good looks like

- The best operator writes the headline from the search term or the ad the visitor clicked.
- The mediocre version adapts the home page and adds a form.
- Good output is a brief a designer and developer can build without a meeting, and a page the weekly report can see.

## Rules

- MUST state one job and one source.
- MUST clear every proof block through `permission-check`.
- MUST include the tracking requirements from `lead-source-audit`.
- NEVER use a mocked or generated product image.
