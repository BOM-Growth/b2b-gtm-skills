---
name: homepage-rewrite
description: Rewrite a B2B company's homepage and the few pages around it so the site says who it is for, what it replaces and why it is better in the first five seconds, and so every form and booking link lands in the CRM. Use when positioning has changed and the site still says the old thing, when the founder says "the website doesn't say what we do", "rewrite the homepage", "our site is generic", "nobody converts", "fix the website copy", or when launching to a new segment. Runs after positioning-doc and offer-and-pilot. Writes the words and the page plan; a separate build step puts them live.
title: Homepage rewrite
collection: website-and-conversion
type: play
playbook: 6
stage: build
---

# Homepage rewrite

Goal: a buyer in the wedge segment lands on the homepage and, without scrolling, knows this is for them, what it does, and what to do next. Messaging is the highest-impact thing on the site. Design makes it trusted on a quick scan. Everything else is secondary.

## Before you start

This skill works on its own. If the person has their own marketing brain folder, read the positioning, messaging, offers and ideal customer files; the homepage is written from them. If they do not have one, ask for any positioning or offer notes they have and the current site URL. If there are no notes, ask the four positioning questions in the session (what do you sell, who is it for, what does it replace, why is it better) and one more: what is the first step a buyer takes. That is enough to write the page; `positioning-doc` goes deeper if they want it later.

Read the current site as a buyer would. Five seconds on the homepage: who is it for, what is it, why better, what next. Write down what the page actually says versus what the positioning says. That gap is the job.

Tools this skill uses when the person has them.

| Step | Tool | What for |
| --- | --- | --- |
| Current performance | Google Analytics 4, Search Console, Microsoft Clarity or Hotjar | Top pages, where visitors come from, what they click, where they leave |
| Copy | Google Docs or markdown | The page copy, one file per page, with the section order |
| Build | WordPress with a page builder; Webflow; Framer; a static site on Netlify | Where the pages get built; the skill writes for whichever one they have |
| Forms and booking | HubSpot forms and meetings, or Pipedrive web forms and a Calendly or Google Calendar booking link | So every lead lands in the CRM with a source |
| Design | Canva or Figma for mockups; the company brand kit | The visual pass once the words are set |
| Images | Their own product screenshots and photos; Higgsfield or similar for generated visuals when there are none | No stock photos of handshakes |

## Steps

1. Set the job of each page. Homepage: tell the wedge buyer it is for them and send them to one action. One page per pillar or use case, if needed. Pricing or offer page. About page. One conversion page (book a demo, start a pilot, get a quote). Anything else is optional and goes in a later pass. Write the job of each page in one sentence before writing copy.

2. Write the homepage above the fold. Four elements:
   - Headline: who it is for and the outcome, in the customer's words from the language bank. Under twelve words.
   - Subheadline: what it is and what it replaces. One or two sentences.
   - The one action: the first step from the offer page, as a button. Only one primary button.
   - Proof line: one logo row, one number, or one quote. Real only.

3. Write the rest of the homepage in this order, one section each, short:
   - The problem as the customer describes it (three to four lines, their words).
   - How it works in three steps.
   - The pillars, one block each: claim, two supporting points, proof.
   - Who it is for, naming the segment and the roles, with a line on who it is not for.
   - Proof: case study summary or testimonials, approved only.
   - The offer in brief: what is included, how pricing works or a from-price, the first step.
   - Objection block: the two or three most common objections answered in a line each (often as a short FAQ).
   - Final action: the same one button, with a line on what happens after they click.

4. Write the conversion page. Headline that restates the first step, three lines on what happens next, the form or booking embed, and one proof element. Keep the form to the fields the CRM needs to qualify: name, work email, company, and one qualifying question from the ICP rules. Everything else can be asked on the call.

5. Write the supporting pages from the positioning doc. Pillar or use-case pages take their pillar section and expand it with proof and a worked example. The about page tells why the company exists and who is behind it, in plain words, and ends with the same action.

6. Plan the forms and tracking. Every form and booking link goes to the CRM, not an inbox. Each one carries a source (page name) and the UTM parameters pass through. Phone numbers on the site are tracked if the company gets calls. Write the list: form, where it lives, what it creates in the CRM, who gets notified, and the follow-up rule. This is handed to `crm-setup`.

7. Set the design direction. Not the design itself: the rules. The brand kit, one accent colour, real product and people imagery, white space, headings a buyer can skim, no walls of text, no generic AI-looking visuals. If the company has a design system, point the builder to it. Mockups come after copy is approved, never before.

8. Write the build brief. For each page: the copy file, the section order, the components, the form or embed, the links. Say which builder it is for. If the person wants the page built here and the builder is one you can write for, build it from the brief; otherwise hand the brief to whoever builds.

9. QA before launch. Headline test with three people who match the ICP: can they say who it is for after five seconds. Form submission test end to end into the CRM. Mobile check. Every link. Page speed. Then launch, and note the date so before-and-after numbers can be compared.

## Rules

- The homepage is for the wedge segment. Other segments get a page, not a watered-down homepage.
- One primary action per page.
- Customer words for the problem, company words for the solution. No "innovative", "leading", "solutions", "empower".
- Real proof only. No placeholder logos, no invented numbers, no quotes without approval.
- Every form into the CRM with a source. A form that emails an inbox is a leak.
- Copy first, design second. Do not mock up until the words are approved.
- Launch and iterate. A better headline next month beats a perfect one in three.

## Output

Return the page plan with the job of each page, the homepage copy by section, the conversion page copy, the supporting page copy, the forms and tracking list, the design direction, the build brief, and the launch QA checklist.

If the person has their own marketing brain folder, save to it:
- `4-playbooks/` as `website.md`: the page plan, the form list and the QA checklist
- `3-strategy/messaging.md`: the final headline and subheadline, dated
- `5-current/decisions-log.md`: the launch date and what changed

If they do not have one, return the copy and the build brief as files. Do not set up a brain unless they ask.

Next: `crm-setup` wires the forms. `creative-brief-library` and `outbound-list-and-sequence` reuse the headline and proof. A conversion pass on the live pages can use any page or form optimisation skill the person already has.
