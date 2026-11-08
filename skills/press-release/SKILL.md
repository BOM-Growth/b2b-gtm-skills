---
name: press-release
title: Press release
description: |
  Use this skill to write the release itself: "draft the press release", "the
  announcement for the wire", "the release for the partnership", "the funding
  announcement", "the customer win release". Produces the release in standard form
  (headline, subhead, dateline, lede, proof, quotes, boilerplate, contact) with every
  claim cleared and the voice rules applied.
collection: search-aeo-and-pr
type: play
reads: [2-standards/proof-rules.md, 2-standards/brand-voice.md]
related: [paid-search-pr, pr-brief, trade-press-placement, brand-voice, founder-voice, permission-check]
playbook: 12
stage: distribution
---

This applies after `pr-brief` sets the angle. It produces a release that reads as news, not as a product page.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` in the header first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact; a blank is a question for the person.

Tools: this play speaks in verbs (check the CRM, pull the call, schedule the post). `TOOLS.md` at the root of this repo lists the tools recommended for each verb. The company's own `1-context/stack.md` wins when it exists. No tool is required; a spreadsheet and a mail client cover most of it.

## The play

1. Read the context (see Before you start) and the `pr-brief` output. Take the angle, proof, spokesperson and quotes as given; do not invent new ones here.
2. Headline: the change for the reader in ten words or fewer, no company adjectives. Subhead: the proof.
3. Dateline and lede: who, what, when, why it matters, in one paragraph a reporter could lift.
4. Body: two to four paragraphs. Proof first (the cleared number, the customer, the scale), then how it works in one paragraph, then availability and pricing posture.
5. Quotes: the spokesperson's quote says why, in their voice through `founder-voice`; the customer's quote says what changed, exactly as cleared in the proof tracker; a partner's quote if the brief has one.
6. Boilerplate from `brand-voice`; media contact; links.
7. Run `brand-voice` for banned patterns and superlatives. Run `permission-check` once more on the final text.
8. Deliver with a short cover note for the human who will send it, and the embargo line if there is one.

## What good looks like

- The best operator writes the headline a trade editor would keep.
- The mediocre version leads with "is proud to announce" and buries the proof in paragraph four.
- Good output is a release where every sentence could be printed as written.

## Rules

- MUST take the angle and proof from `pr-brief`; no new claims introduced here.
- MUST run `permission-check` on the final text.
- NEVER quote a customer outside the exact cleared wording.
- NEVER distribute; the human sends.
