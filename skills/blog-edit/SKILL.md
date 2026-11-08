---
name: blog-edit
title: Blog edit
description: |
  Use this skill to get a long-form piece ready to publish: "clean up this article",
  "fix the links", "add internal CTAs", "find real sources for these claims", "make it
  ready to publish", "polish the draft", "this was ghostwritten". Produces the edited
  article with bare URLs turned into anchor text, weak citations replaced with
  verifiable sources, internal links and customer-story CTAs added, banned patterns
  removed, and the naming checked.
collection: content-and-proof
type: play
reads: [2-standards/brand-voice.md, 2-standards/proof-rules.md, 1-context/stack.md]
related: [content-proof, brand-voice, permission-check, aeo-review, content-calendar]
playbook: 10
stage: distribution
---

This applies before any article ships. It produces a piece that teaches, cites, and sends the reader somewhere useful.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start). Read the draft once for the argument: what does the reader leave with? If there is no answer, send it back with that note.
2. Sources: every statistic, study or market claim gets a verifiable source (peer-reviewed, industry body, government, a named report). Replace vague "studies show" with the source or cut the claim. Open the source; do not cite from a search snippet.
3. Links: turn bare URLs into anchor text; check every link resolves; add two to four internal links to related articles and one customer-story CTA where the topic fits.
4. Customer mentions: through `permission-check`. Role-only attribution where not cleared.
5. Voice: run `brand-voice` for banned patterns, naming, and headline rule (section headings state the point, not the topic).
6. Structure for search and AI answers: a clear answer in the first paragraph, headings that match how people ask, a short summary block if `aeo-review` recommends it.
7. Return the edited article with a short change log: sources replaced, links added, patterns removed, open questions for the author.

## What good looks like

- The best operator reads the citations before the prose. An article with a confident claim and no source is the one that gets quoted back at the company.
- The mediocre version fixes typos and leaves "research shows" in place.
- Good output is an article where every number has a link, every heading makes a point, and the reader has somewhere to go next.

## Rules

- MUST verify every cited source by opening it.
- MUST run `permission-check` on every customer mention.
- NEVER leave a bare URL or a "studies show" without a source.
- NEVER publish with a name that is not on the current naming list.
