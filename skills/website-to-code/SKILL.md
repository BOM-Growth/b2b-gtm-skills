---
name: website-to-code
title: Move a website to code
description: |
  Use this skill when someone is tired of learning and fighting their website tool and
  wants to change their site by asking an AI agent in plain language instead. Moves the
  site off a legacy website tool (WordPress and its page builders, Squarespace, Wix,
  Webflow, HubSpot CMS, Duda, or a custom site nobody can maintain) and into code in a
  GitHub repo the agent edits. Triggers: "move our site to code", "port the website
  to GitHub", "rebuild the site in Claude Code", "get off WordPress", "get off
  Squarespace", "make the site agent friendly", "can AI just maintain the website",
  "host it on Netlify".
  Produces the content and design pulled from the old site, the SEO inventory and
  redirect map, the rebuilt site in a repo, the technical SEO fixes, a preview link to
  review, and the launch.
collection: website-and-conversion
type: play
reads: [1-context/company.md, 1-context/stack.md, 2-standards/brand-voice.md]
related: [homepage-rewrite, landing-page-brief, crm-setup, seo-audit, aeo-review]
playbook: 6
stage: build
---

The goal: manage the website by asking an AI agent in plain language, instead of learning and working a website tool. Even drag-and-drop editors take hours to learn and time to use; once the site is code in a repo, a change is a sentence to the agent and a preview link to approve.

When to use it: the site lives in a tool that is slow, expensive or hard to change. Produces the same site, rebuilt in a GitHub repo, live on the same domain, with its search rankings kept and its technical SEO fixed on the way.

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` first and cite them for every fact. If they do not have one, do not look for one: ask for the current site URL, which tool it is built on, and whether they can log in to it. Never invent a fact.

Ask whether this is a move (same pages, same words, new home) or a move and a rewrite. Do not combine them unless the person says so. If the words are changing, run `homepage-rewrite` for the copy and use this skill for the move.

Tools: GitHub for the repo; Claude Code (or Codex, Cursor) to build; Netlify, Vercel or Cloudflare Pages to host and give preview links; Google Search Console, the sitemap and a crawler such as Screaming Frog for the SEO inventory; PageSpeed Insights for speed. See TOOLS.md. None are required beyond a repo and a host.

## The play

1. Read the context. Take the brand rules, the voice, the CRM and the tracking setup from it.

2. Get the content and design. Use whichever route the old tool allows; use both when you can.
   - Download the data. Most tools have an export: WordPress gives an XML file of pages and posts plus the media library; others export pages, posts or a CSV of collection items. An export gets the words, dates and images cleanly.
   - Point at the live site. Crawl every page and read the rendered HTML and CSS. This works on any tool, even without a login, and it is the best source for the components: header, footer, hero, card, testimonial, form, and how each looks on desktop and mobile.

   Save each page as a markdown file with its title, description, date and URL. Download every image and document the pages use. Keep the words exactly as they are unless a rewrite was agreed.

3. Pull the design system. From the builder settings or the live CSS, take the colours, fonts, sizes, spacing, buttons and logo, and write them into one tokens file. If the company has a brand kit, the brand kit wins over what the old site happens to use. List the components the site repeats; these become the building blocks of the new site.

4. Build the SEO inventory. The menu is not the list of pages. Merge, into one sheet:
   - Search Console: every indexed page, with clicks and impressions over the last 12 months, and any pages it flags with errors.
   - The sitemap (`/sitemap.xml` and the variants the tool uses).
   - A full crawl: status codes, titles, meta descriptions, H1s, canonical tags, structured data, image alt text, internal links, broken links and redirect chains.

   Add a column for the new URL. Pages with clicks or inbound links are the ones that must not break. Read `references/redirects-and-launch.md` for how to write the redirect map.

5. List the technical fixes. From the crawl, Search Console and PageSpeed Insights, write down the quick wins to fix during the rebuild: missing or duplicate titles and descriptions, missing H1s, broken links, redirect chains, oversized images, slow pages, missing alt text, missing or wrong canonical tags, missing structured data, pages blocked by mistake. Fix these in the new build rather than copying them over. Leave content and keyword strategy for `seo-audit`.

6. Set up the repo so the agent builds on brand. Create a GitHub repo for the site and write, at the root:
   - `CLAUDE.md` (or `AGENTS.md`): what the site is for, the stack, how to run and preview it, where content lives, and what never to change without asking (the tracking container, the form endpoints, the redirect file).
   - The tokens file from step 3.
   - The voice rules from the company's brand voice file.
   - Design rules that keep the site from looking generic: the brand's own fonts, no default gradients, no rows of identical icon cards, no stock photos, varied section layouts.

7. Rebuild. Use a framework built for content sites (Astro is a good default; Next.js when the site needs app features). Build the shared layout and components first, then one page of each type for review, then the rest. Every page carries its title, meta description, canonical URL, social sharing image and structured data. Generate the sitemap and robots.txt from the build. Compress and resize images.

8. Rewire forms and tracking. Every form posts to the CRM with the page name as the source and UTM parameters passed through. Install the same Google Tag Manager container (or analytics tags) the old site used, so reporting, ad pixels and conversions keep working. Booking links stay the same.

9. Review on a preview link. Connect the repo to the host. Every change gets a preview link before anything touches the live site. Put the old and new sites side by side and check every page on the inventory: content, images, mobile layout, forms, and the redirect map run against the preview. The person signs off on the preview link, not on screenshots.

10. Launch. Follow the checklist in `references/redirects-and-launch.md`: redirects live, domain switched, sitemap resubmitted in Search Console, forms tested into the CRM, tracking checked. Keep the old site reachable on a private URL for 30 days.

11. Run it from the repo. Nobody needs to learn the old tool or a new one. From now on a change is:
   - Say what you want in plain language: "add a page for the new service", "swap the hero photo", "fix the typo on pricing".
   - The agent makes the change on a branch.
   - The host builds a preview link.
   - A person checks the preview, approves and merges.

   For the first month, check Search Console weekly and add a redirect for each 404 that matters. At 30 days, compare search clicks, speed scores and form submissions to the month before.

## What good looks like

- Search traffic the month after launch is in the normal range of the month before, and the speed scores and crawl errors are better.
- Content came from the export where one existed and from the live site for everything else, so nothing was retyped.
- The URL list came from Search Console, the sitemap and a crawl. The mediocre version redirects the menu pages and sends the rest to the homepage.
- The person who used to avoid editing the site has made a change by asking the agent, and approved it on a preview link, before the project is called done.
- The repo had a `CLAUDE.md` and a tokens file before the first page was built, so the last page looks like the first.
- Anything that is really an app (a login area, a store, a searchable database) was kept on the old system or scoped as its own project, not squeezed into the move.

## Rules

- MUST cite the context file for every fact when a brain exists; say when a fact is missing.
- MUST build the URL list from Search Console, the sitemap and a crawl, and give every URL with traffic or links its own 301 redirect.
- MUST carry over titles, descriptions, H1s and structured data, and fix the technical issues found, not copy them.
- MUST keep the same tracking and send every form to the CRM.
- MUST review every change on a preview link before it goes live.
- NEVER redirect old URLs in bulk to the homepage.
- NEVER change page copy during the move unless a rewrite was agreed.
- NEVER switch the domain before the preview is signed off and the forms are tested.

## Output

Return, in order: the content and asset export; the tokens file and component list; the SEO inventory and redirect map as a spreadsheet; the technical fix list with each item marked done; the repo with `CLAUDE.md`; the preview link; the launch checklist with each item checked; and the steps for requesting changes from now on.

If the person has their own marketing brain, save the launch date and what changed to `5-current/decisions-log.md` and the new stack to `1-context/stack.md`. If not, return them as files they can keep. Do not set up a brain unless they ask.
