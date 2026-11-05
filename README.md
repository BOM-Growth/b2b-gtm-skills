# B2B GTM Skills

A transportable go-to-market playbook for B2B companies, written as agent skills. Nineteen playbooks in the order a company meets them, 98 skills that each work on their own, and a marketing brain template that gives every skill the company's context. Every skill is a plain `SKILL.md` that Claude, Claude Code, Codex, Cursor or any agent on the Agent Skills spec can read, or that you can paste into any chat assistant.

Written by Matt Santos at BOM Growth from running these playbooks inside B2B companies, from first customers to a built-out marketing function. Free to use and share under the MIT license.

## What is different about this library

- It is in order. Most skill libraries are a flat list of tactics. This one is the sequence a company actually runs: learn, lay the foundations, put them where buyers see them, make it trackable, go get customers by hand, turn on channels, measure every 90 days, resource it and hand it off. Start where your company is.
- Every skill works on its own. Install one and get value today. Install the set and they hand off to each other.
- Context lives in a folder, not a prompt. The marketing brain is one folder of plain files about your business that every skill reads first and writes back to. Skills never assume it exists; they ask when it does not.
- Tools are recommended, never required. Skills speak in verbs (check the CRM, pull the call). `TOOLS.md` says which tools work well for each verb; your own stack file wins.
- Humans stay in the loop. Nothing reaches a customer, a prospect or the public without a person reading it. No customer name, quote, logo or number is used without approval.

## Layout

```
playbooks/                 the order of operations: one folder per playbook, each with a human SOP page
  0-foundation/  1-build/  2-distribution/  3-operate/
skills/                    one folder per skill, flat, each with SKILL.md (and references/ where depth is needed)
marketing-brain-template/  the empty context folder a company copies into Drive or a repo
templates/skill/           the SKILL.md template for writing a new skill in the same shape
TOOLS.md                   recommended tools by verb
CLAUDE.md, AGENTS.md       instructions for agents running the skills
validate-skills.py         checks every skill's frontmatter and conventions
```

## How to use it

1. Pick the playbook that matches where your company is (the index below). Read its `SOP.md`: what it produces, why, the order, who is involved, how long it takes.
2. Run the skills in it. Each one tells the agent what to ask you, what to do, and what to hand back.
3. Set up the marketing brain when you are tired of re-explaining your business. Copy `marketing-brain-template/` into Google Drive, OneDrive, SharePoint or a repo and run the `marketing-brain` skill. From then on every skill reads it and files to it.

## Install

```bash
# everything, for Claude Code
npx skills add BOM-Growth/b2b-gtm-skills -a claude-code

# one skill
npx skills add BOM-Growth/b2b-gtm-skills --skill icp-and-wedge

# as a Claude Code plugin
/plugin marketplace add BOM-Growth/b2b-gtm-skills
/plugin install b2b-gtm-skills
```

No CLI: open any `skills/<name>/SKILL.md`, copy all of it, paste it into your assistant, and answer its questions.

## Skill types

| Type | What it is |
| --- | --- |
| foundation | Read by other skills: the context loader, the permission check, the decision log, the voices |
| playbook | An entry point that routes to plays in order for a recurring motion (outbound, events, launch) |
| play | One job, one output |
| loop | A scheduled run that calls a playbook (daily brain sweep, weekly channel update) |

## The playbooks and their skills


### 1. Discovery and diagnosis

Stage: foundation. SOP: `playbooks/0-foundation/01-discovery-and-diagnosis/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`call-mining`](skills/call-mining/SKILL.md) | play | Turn recorded sales, customer and discovery calls into go-to-market intelligence: the words customers use for the problem, objections and how they were handled, competitors named, why deals were won or lost, feature requests, and quotes that can become proof. |
| [`customer-interview`](skills/customer-interview/SKILL.md) | play | Before and during a customer interview for a story, a testimonial or a launch quote: "prep the interview", "questions for the customer call", "the prep doc", "what to ask", "pre-call email". |
| [`gtm-diagnostic`](skills/gtm-diagnostic/SKILL.md) | play | Produce the 30-day read of a B2B company's go-to-market: where it stands on product, market, customers, funnel, tracking, channels, assets and team, where the leaks are, and the quick wins to do first. |

### 2. Marketing brain

Stage: foundation. SOP: `playbooks/0-foundation/02-marketing-brain/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`decision-log`](skills/decision-log/SKILL.md) | foundation | When a GTM decision gets settled in a chat, a call or a review: a naming rule, a claim retired, a reward amount, a hero line, a segment added, a channel paused. |
| [`gtm-context`](skills/gtm-context/SKILL.md) | foundation | When a question or task touches the company's go-to-market facts: who we sell to, what we claim, how we sound, which tool holds which record, what the funnel stages mean, what the calendar allows. |
| [`marketing-brain`](skills/marketing-brain/SKILL.md) | play | Set up and maintain a marketing brain, a folder of plain text files about a business that an AI assistant reads before doing any marketing work. |
| [`daily-brain-sweep`](skills/daily-brain-sweep/SKILL.md) | loop | Every morning: "the morning sweep", "what changed overnight", "update the brain", "anything new from the calls yesterday". |

### 3. ICP and wedge

Stage: foundation. SOP: `playbooks/0-foundation/03-icp-and-wedge/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`icp-lists`](skills/icp-lists/SKILL.md) | playbook | Anything about who we target: "review the ICP", "are we targeting the right accounts", "build a list for", "is this account a fit", "filter these leads", "tier my accounts", "who should we go after", "what's our TAM". |
| [`audience-icp-filter`](skills/audience-icp-filter/SKILL.md) | play | When a list already exists and someone needs to know who on it is worth contacting: event scans, webinar registrants, an association member list, a partner's leads, a newsletter export. |
| [`build-target-list`](skills/build-target-list/SKILL.md) | play | When a play needs accounts or contacts: "build a list for the show", "who's in the association", "ad audience for", "this week's cohort", "target accounts in Texas", "everyone in the TAM who", "contacts at these companies". |
| [`icp-and-wedge`](skills/icp-and-wedge/SKILL.md) | play | Choose the first customer segment to go after (the wedge), define the ideal customer profile, map the buying committee and write qualification rules a person or an agent can apply. |
| [`icp-fit-check`](skills/icp-fit-check/SKILL.md) | play | When one account needs a verdict: "is this a fit", "should we take this demo", "tier this account", "is this company in our ICP", "they're small, do we still want them", "check them against the TAM". |

### 4. Positioning and messaging

Stage: foundation. SOP: `playbooks/0-foundation/04-positioning-and-messaging/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`brand-voice`](skills/brand-voice/SKILL.md) | foundation | When writing or reviewing any piece in the company's voice: a post, an email, an ad, a page, a one-pager, a script. |
| [`founder-voice`](skills/founder-voice/SKILL.md) | foundation | When drafting or rewriting anything that carries the founder's own name: personal posts, panel intros, podcast pitches, speaker bios, founder quotes in a case study. |
| [`positioning-doc`](skills/positioning-doc/SKILL.md) | play | Write the full positioning and messaging document for a B2B company: the four positioning questions answered in full, the problem and what the product replaces, differentiation, messaging pillars, a stakeholder messaging matrix for the buying committee, objections with answers, and proof points. |
| [`positioning-one-liner`](skills/positioning-one-liner/SKILL.md) | play | Write a one-sentence description of a business that a stranger can repeat to someone else. |

### 5. Offer and pricing

Stage: foundation. SOP: `playbooks/0-foundation/05-offer-and-pricing/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`offer-and-pilot`](skills/offer-and-pilot/SKILL.md) | play | Package what a B2B company sells into an offer the first customers in the wedge can say yes to: what is included, what it costs, how it is delivered, the pilot or first-step terms, and the one-sentence ask. |

### 6. Website and conversion

Stage: build. SOP: `playbooks/1-build/06-website-and-conversion/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`graphics-check`](skills/graphics-check/SKILL.md) | play | Before any image, social graphic, banner or one-pager ships: "is this on brand", "check the graphic", "resize for the other channels", "the screenshot is cut off", "can we generate an image for this". |
| [`homepage-rewrite`](skills/homepage-rewrite/SKILL.md) | play | Rewrite a B2B company's homepage and the few pages around it so the site says who it is for, what it replaces and why it is better in the first five seconds, and so every form and booking link lands in the CRM. |
| [`landing-page-brief`](skills/landing-page-brief/SKILL.md) | play | Before any page is built or changed: "a landing page for", "the demo page isn't converting", "a page for the campaign", "the comparison page", "the pricing page copy", "rewrite the home page". |
| [`leave-behind-page`](skills/leave-behind-page/SKILL.md) | play | For the one page a rep sends after a conversation: "the leave-behind", "what do we send after the demo", "a one-pager", "the page for the event follow-up", "something the champion can forward to their boss". |

### 7. Sales enablement

Stage: build. SOP: `playbooks/1-build/07-sales-enablement/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`discovery-and-demo`](skills/discovery-and-demo/SKILL.md) | play | Build the discovery call structure, qualification questions, demo script and deck outline for a B2B sale, so every call runs the same way and ends with a clear next step. |
| [`sales-command-center`](skills/sales-command-center/SKILL.md) | play | Build the one page a salesperson works from: the sales process in order with every script, asset, pricing range, template and link embedded at the step where it is used, plus the testimonial and case study request process. |

### 8. CRM and tracking

Stage: build. SOP: `playbooks/1-build/08-crm-and-tracking/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`inbound-lifecycle`](skills/inbound-lifecycle/SKILL.md) | playbook | Every hand-raise and every email the company sends to people it already knows: "a demo request came in", "triage this lead", "where did this lead come from", "attribution", "the routing form", "nurture email", "customer email", "the weekly send", "landing page for", "send me something to look at". |
| [`crm-setup`](skills/crm-setup/SKILL.md) | play | Set up or clean up a B2B company's CRM so the pipeline is real, every lead lands in it with a source, nothing slips through the cracks, and the numbers can be trusted: stages, lifecycle, properties, forms and booking links, one sequencing tool, routing and follow-up rules, and the reports the weekly meeting reads. |
| [`demo-routing`](skills/demo-routing/SKILL.md) | play | When a fit lead needs a rep and a slot: "route this demo", "who owns this account", "the demo didn't get booked", "the handoff to sales", "round robin", "the rep brief for tomorrow's demo". |
| [`funnel-definitions`](skills/funnel-definitions/SKILL.md) | play | Whenever a number's meaning is in question: "what counts as an MQL", "define SQL", "why do sales and marketing numbers differ", "is a demo request a lead", "the stage definitions", "set up the funnel fields". |
| [`inbound-triage`](skills/inbound-triage/SKILL.md) | play | On every inbound lead: "a demo request came in", "triage the inbound", "is this lead real", "who should take this", "the form submissions this week". |
| [`lead-source-audit`](skills/lead-source-audit/SKILL.md) | play | When the source numbers cannot be trusted: "where are leads coming from", "attribution is broken", "the source field is empty", "the form isn't tagging", "what did paid actually produce", "the CRM says direct for everything". |

### 9. First customers and outbound

Stage: distribution. SOP: `playbooks/2-distribution/09-first-customers-and-outbound/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`outbound`](skills/outbound/SKILL.md) | playbook | Prospecting and re-engagement with sales: "next cohort", "who do we email this week", "re-engage closed lost", "pricing campaign", "win-back", "sequence copy", "signal-based outbound", "website visitors", "new followers", "we have the signal, we just have to execute". |
| [`outbound-cohort`](skills/outbound-cohort/SKILL.md) | play | At the start of each outbound week: "next cohort", "who do we go after this week", "cold, warm or closed lost", "bottom-up or top-down", "what's the angle for this group". |
| [`outbound-list-and-sequence`](skills/outbound-list-and-sequence/SKILL.md) | play | Build a prospect list that matches the target customer, verify it, write the cold email and follow-up sequence in the company's voice, set the rules for handling replies, and hand qualified replies into the CRM. |
| [`outbound-sequence-copy`](skills/outbound-sequence-copy/SKILL.md) | play | When a cohort needs words: "write the sequence", "cold email for", "follow-up emails", "the win-back email", "call script for the exec rung", "beat up this sequence". |
| [`reply-handling`](skills/reply-handling/SKILL.md) | play | When outbound replies come in: "they replied", "what do I say back", "interested but not now", "they asked for pricing", "out of office", "wrong person", "the calendar is full". |
| [`signal-to-outreach`](skills/signal-to-outreach/SKILL.md) | play | When a buying signal fires: a new follower from an ICP account, an identified website visitor, a prospect mentioned on a customer call, a job posting for the role we sell to, a competitor mention. |
| [`top-100-list`](skills/top-100-list/SKILL.md) | play | Build a list of 100 people who might know a buyer and draft the message to send them. |

### 10. Content and proof

Stage: distribution. SOP: `playbooks/2-distribution/10-content-and-proof/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`permission-check`](skills/permission-check/SKILL.md) | foundation | Before any customer name, logo, quote, number or story appears in a piece, and when someone asks "can we use X", "is this quote approved", "can we name them", "is that number cleared". |
| [`content-proof`](skills/content-proof/SKILL.md) | playbook | The content engine and customer proof: "content calendar", "what are we posting", "post ideas", "founder post", "company page", "blog", "case study", "testimonial", "customer story", "video", "clip", "did you know", "the quote bank". |
| [`blog-edit`](skills/blog-edit/SKILL.md) | play | To get a long-form piece ready to publish: "clean up this article", "fix the links", "add internal CTAs", "find real sources for these claims", "make it ready to publish", "polish the draft", "this was ghostwritten". |
| [`call-to-content`](skills/call-to-content/SKILL.md) | play | Turn sales calls, customer calls, internal discussions and existing material into a steady stream of posts, articles and emails in the founder's voice, with a simple approval and posting routine. |
| [`case-study`](skills/case-study/SKILL.md) | play | For a customer story from candidate to published: "write a case study", "customer story for", "success teed up a candidate", "prep for the interview", "clip log", "co-marketing posts from the case study", "track the case study pipeline". |
| [`content-calendar`](skills/content-calendar/SKILL.md) | play | To plan or change what gets published: "what's on the calendar", "move that post", "add the launch posts", "we need something for the show", "fill next week", "what's the plan for the blog". |
| [`customer-video-cut`](skills/customer-video-cut/SKILL.md) | play | When customer footage needs cutting: "cut the interview", "make clips from the testimonial", "a vertical version", "the booth loop", "add captions", "it shipped silent". |
| [`endless-idea-generator`](skills/endless-idea-generator/SKILL.md) | play | Generate 100 social media or content post ideas from two short lists, pick the best three, and draft them. |
| [`founder-content-rhythm`](skills/founder-content-rhythm/SKILL.md) | play | Weekly for the founder's own content: "ideas for this week's posts", "what did the founder see this week", "prep the content meeting", "finalize the founder's drafts", "schedule next week's founder posts". |
| [`product-tip-series`](skills/product-tip-series/SKILL.md) | play | For the recurring feature-tip series to customers and followers: "did you know post", "feature tip this week", "a short on the new tool", "customers don't know this exists", "what shipped that we haven't talked about". |
| [`proof-capture`](skills/proof-capture/SKILL.md) | play | The moment proof appears: a quote on a call, a video testimonial submitted, a number a customer states at a booth, a positive line in an email, a review. |
| [`schedule-post`](skills/schedule-post/SKILL.md) | play | When approved posts need to go out: "schedule these", "post it Thursday", "queue next week's posts", "move the post to Friday", "is it scheduled". |
| [`social-post`](skills/social-post/SKILL.md) | play | For company page posts: "draft a post about", "turn this into a post", "posts from this transcript", "a batch of posts for the launch", "event post", "customer post", "revise this post". |
| [`founder-weekly-ideas`](skills/founder-weekly-ideas/SKILL.md) | loop | Every week before the founder's writing slot: "ideas for this week's posts", "what should I write about", "the founder content prompts", "what happened that's worth a post". |

### 11. Paid channels

Stage: distribution. SOP: `playbooks/2-distribution/11-paid-channels/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`paid-search-pr`](skills/paid-search-pr/SKILL.md) | playbook | Paid search, paid social, organic search and AI answers, and earned media: "the ads", "paid is failing", "audit the account", "ad copy", "spend by channel", "SEO", "AEO", "are we showing up in AI answers", "press release", "PR agency", "trade press", "awards". |
| [`ad-copy`](skills/ad-copy/SKILL.md) | play | For any paid placement's words: "headlines for the search ads", "ad copy for", "a thought leader ad", "the print ad for the trade magazine", "critique these ads", "the display assets". |
| [`creative-brief-library`](skills/creative-brief-library/SKILL.md) | play | Build a reusable library of ad angles and creative briefs for a B2B company, with a test-then-scale routine so paid spend goes to what converts. |
| [`google-ads`](skills/google-ads/SKILL.md) | play | To run or audit paid search for B2B: "the search campaigns", "search term report", "negatives", "competitor ad group", "quality score", "the landing page for ads", "CPCs are up", "shift budget between campaigns", "take the account back from the agency". |
| [`linkedin-ads`](skills/linkedin-ads/SKILL.md) | play | To run or audit paid social for B2B: "the social ads", "thought leader ads from the founder", "the audience is too small", "are we over-serving", "frequency", "which accounts engaged", "the monthly ads report", "conversion tracking". |
| [`paid-weekly-report`](skills/paid-weekly-report/SKILL.md) | play | Every week for paid channels: "spend by channel", "how are the ads doing", "cost per demo", "what's the paid update", "are the ads working yet". |

### 12. Search, AEO and PR

Stage: distribution. SOP: `playbooks/2-distribution/12-search-aeo-and-pr/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`aeo-review`](skills/aeo-review/SKILL.md) | play | To check how the company shows up where buyers now ask: "are we in the AI answers", "what does the assistant say about us", "our competitor shows up and we don't", "AEO", "the prompts buyers ask", "llms.txt". |
| [`awards-submission`](skills/awards-submission/SKILL.md) | play | When an award, ranking or list is worth entering: "should we apply for", "the awards deadline", "the industry innovation award", "best places to", "the top vendors list", "the nomination form". |
| [`pr-brief`](skills/pr-brief/SKILL.md) | play | When something is worth telling the press: "is this newsworthy", "the PR angle for", "brief the PR agency", "which outlets for", "what's the story". |
| [`press-release`](skills/press-release/SKILL.md) | play | To write the release itself: "draft the press release", "the announcement for the wire", "the release for the partnership", "the funding announcement", "the customer win release". |
| [`seo-audit`](skills/seo-audit/SKILL.md) | play | For organic search: "SEO audit", "why did organic drop", "what should we write for search", "the site's technical health", "keyword gaps", "the blog isn't ranking". |
| [`trade-press-placement`](skills/trade-press-placement/SKILL.md) | play | To get into the publications the ICP reads: "pitch the trade magazine", "a bylined article for", "get the case study into the industry publication", "the editorial calendar", "who covers our space". |

### 13. Email and lifecycle

Stage: distribution. SOP: `playbooks/2-distribution/13-email-and-lifecycle/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`closed-lost-winback`](skills/closed-lost-winback/SKILL.md) | play | When something has changed that answers a past objection: a release, a pricing change, a new package, a segment opened. |
| [`customer-update-email`](skills/customer-update-email/SKILL.md) | play | For email to existing customers: "the monthly customer update", "the release notes email", "tell customers about", "the newsletter", "the product update email for". |
| [`nurture-email`](skills/nurture-email/SKILL.md) | play | For the emails to leads who are not ready: "the nurture sequence", "what do we send the leads who didn't book", "the post-webinar sequence", "the event leads that went cold", "a drip for", "re-engage the old leads". |
| [`reengage-old-leads`](skills/reengage-old-leads/SKILL.md) | play | Go back to closed-lost deals, stale opportunities and old leads with a real reason to talk again (new pricing, new features, a new offer, a result they asked for) and turn the ones whose situation changed into pipeline. |

### 14. Events

Stage: distribution. SOP: `playbooks/2-distribution/14-events/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`events`](skills/events/SKILL.md) | playbook | Trade shows, conferences, regional and trade association meetings, speaking slots, hosted dinners and webinars: "should we do this show", "what do we need for", "where are we at with the conference", "booth", "attendee list", "lead capture", "follow up from the show", "the association meeting", "speaking deadline". |
| [`association-play`](skills/association-play/SKILL.md) | play | For regional and trade associations: "join the association", "their meeting is next month", "get on their member list", "who runs the association", "speak to their members", "they want us to come speak", "we're caught flat-footed on these events". |
| [`event-debrief`](skills/event-debrief/SKILL.md) | play | In the week after a show and again at the payback horizon: "debrief the show", "how did it go", "what did the conference produce", "was it worth it", "lessons for next year". |
| [`event-follow-up`](skills/event-follow-up/SKILL.md) | play | From the day after a show until every lead has an outcome: "follow up from the show", "where are the event leads", "has anyone contacted them", "the follow-up has been poor", "what happened to the scans". |
| [`event-lead-ingest`](skills/event-lead-ingest/SKILL.md) | play | On every show day and the day after: "process today's scans", "tier the leads", "who did we meet", "get the badge scans into the CRM", "end of day summary", "the scans are a mess". |
| [`event-outreach`](skills/event-outreach/SKILL.md) | play | In the eight weeks before a show: "book meetings before the show", "who do we email about the show", "pre-show campaign", "the booth draw", "attendee list outreach", "tell customers we'll be there", "open deals at the show". |
| [`event-plan`](skills/event-plan/SKILL.md) | play | Once a show is a go and it is more than the minimum lead time out: "plan the show", "what do we need for", "where are we at with", "the checklist", "booth logistics", "who's going", "travel", "sponsorship deliverables". |
| [`event-playbook`](skills/event-playbook/SKILL.md) | play | Run a trade show, conference, dinner or webinar as a pipeline play: choose the event, book meetings before it starts, qualify and capture on site, follow up within days, and report what it produced in leads, meetings and pipeline. |
| [`event-prep-deck`](skills/event-prep-deck/SKILL.md) | play | In the last two weeks before a show: "team prep deck", "prep call for the show", "talk tracks", "what do we say at the booth", "booth rules", "who's on which shift". |
| [`event-scorecard`](skills/event-scorecard/SKILL.md) | play | When deciding whether to exhibit at, attend, sponsor or speak at a show: "should we do this show", "is it worth it", "they want us to sponsor", "which shows next year", "we found out about an event next month". |
| [`speaking-proposal`](skills/speaking-proposal/SKILL.md) | play | When a speaking slot is possible: "the call for speakers is open", "they asked us to present", "submit a session", "the deck for the talk", "co-present with a customer", "we missed the deadline last year". |
| [`webinar-play`](skills/webinar-play/SKILL.md) | play | For events the company hosts: a webinar, a dinner near a show, a workshop, a customer session. |
| [`event-follow-up-check`](skills/event-follow-up-check/SKILL.md) | loop | Daily for two weeks after any event: "where are we on the event leads", "did everyone get followed up", "the post-event check". |

### 15. Measurement and reporting

Stage: operate. SOP: `playbooks/3-operate/15-measurement-and-reporting/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`reporting-experiments`](skills/reporting-experiments/SKILL.md) | playbook | The operating rhythm: "the weekly update", "MQLs by channel", "what happened last week", "spend by channel", "experiment", "A/B test", "what are we testing", "readout", "quarterly plan", "board slides", "Q3 postmortem", "what are the rocks". |
| [`experiment-brief`](skills/experiment-brief/SKILL.md) | play | Before any test starts: "let's try", "should we test", "an experiment on", "run a pilot of", "I want to see if", "a bet on". |
| [`experiment-readout`](skills/experiment-readout/SKILL.md) | play | When a test reaches its readout date: "did the test work", "readout on", "should we keep running", "the results of the pilot", "scale or kill". |
| [`quarterly-gtm-plan`](skills/quarterly-gtm-plan/SKILL.md) | play | At the end of each quarter: "the plan for next quarter", "where should budget go", "what are we doing in Q", "the marketing plan", "the quarterly review". |
| [`scorecard-and-okrs`](skills/scorecard-and-okrs/SKILL.md) | play | Turn a founder's revenue goal into three 90-day objectives with measurable key results, a weekly scorecard where every number has a source, a 30-minute weekly go-to-market meeting that reads it, and a 90-day review that resets the plan. |
| [`weekly-marketing-update`](skills/weekly-marketing-update/SKILL.md) | play | Every week: "the weekly update", "marketing numbers for the leadership meeting", "what did marketing do this week", "the Monday report", "MQLs this week". |
| [`monthly-experiment-readout`](skills/monthly-experiment-readout/SKILL.md) | loop | On the first working day of the month: "the monthly readout", "what did we learn last month", "scale or kill review", "the bets review". |
| [`weekly-channel-update`](skills/weekly-channel-update/SKILL.md) | loop | Every week on the same day: "the Monday numbers", "run the weekly", "channel update". |

### 16. Team, hiring and handoff

Stage: operate. SOP: `playbooks/3-operate/16-team-hiring-and-handoff/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`hire-and-ramp`](skills/hire-and-ramp/SKILL.md) | play | Decide what the next marketing or go-to-market hire should be, write the job post and the scorecard to screen against, build the 30-60-90 day ramp plan, and prepare the handoff package so the function runs without the person who built it. |

### 17. AI-native GTM ops

Stage: operate. SOP: `playbooks/3-operate/17-ai-native-gtm-ops/SOP.md`

No skill of its own; the loops under other playbooks are the practice.


### 18. Launch

Stage: distribution. SOP: `playbooks/2-distribution/18-launch/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`release-to-narrative`](skills/release-to-narrative/SKILL.md) | foundation | When a feature ships, is about to ship, or appears on the roadmap and marketing needs to know what it may say about it: "what can we say about X", "is this newsworthy", "write up the release", "what's the story on the new feature", "what's what changed for the customer". |
| [`launch`](skills/launch/SKILL.md) | playbook | A marketable release: "we're launching", "plan the launch", "the new version", "when do we announce", "what goes out and when", "customers need to hear about this", "rebrand", "relaunch". |
| [`customer-launch-kit`](skills/customer-launch-kit/SKILL.md) | play | When a launch needs customers in it: "get customers posting on launch day", "customer quotes for the release", "co-marketing for the launch", "who can we ask to share", "the launch kit". |
| [`launch-calendar`](skills/launch-calendar/SKILL.md) | play | When a release will be marketed and nobody has landed the date: "when are we launching", "plan the launch dates", "tease, announce, launch", "what goes out when", "the launch is leaking", "customers need to hear first". |
| [`launch-internal-brief`](skills/launch-internal-brief/SKILL.md) | play | Before anything about a release goes external: "brief the team", "what do we tell people if they ask", "talking points for the launch", "a banner is going out tomorrow", "the company needs to know this is happening". |

### 19. Referral and partners

Stage: distribution. SOP: `playbooks/2-distribution/19-referral-and-partners/SOP.md`

| Skill | Type | What it does |
| --- | --- | --- |
| [`referral-partners`](skills/referral-partners/SKILL.md) | playbook | Word of mouth and partner channels: "referral program", "relaunch referral", "the reward", "who referred", "partner leads", "lead sharing", "co-marketing with", "joint webinar", "shared booth". |
| [`co-marketing-campaign`](skills/co-marketing-campaign/SKILL.md) | play | When building something with a partner: "joint webinar with", "share a booth", "cost-share the videographer", "co-branded content", "joint dinner near the show", "a partner newsletter mention". |
| [`partner-lead-exchange`](skills/partner-lead-exchange/SKILL.md) | play | When a partner will share leads: "set up lead sharing with", "they committed ten leads a week", "are they delivering", "what do we owe them", "the SLA with the partner". |
| [`referral-campaign`](skills/referral-campaign/SKILL.md) | play | To launch or refresh a referral program send: "relaunch referral", "blast the referral email", "the reward is now", "open it to non-customers", "make the intro one click", "who gets the referral email". |
| [`referral-tracker`](skills/referral-tracker/SKILL.md) | play | Whenever a referral arrives or someone asks about the program's results: "who referred this", "how many referrals", "do we owe anyone", "pipeline from referral", "pay out the reward". |

## Conventions

- A skill has: frontmatter (name, title, description with trigger phrases, collection, type, reads, related), a Before you start section that makes it standalone, the play in numbered steps, what good looks like, rules, and an output that says where it is saved.
- No em dashes, no buzzwords, no slogans, no emoji. Write how people talk.
- Depth goes in `references/` next to the skill, one to four pages.
- Run `python3 validate-skills.py` before opening a pull request.

## Contributing

Open a pull request with a new skill in the same shape as `templates/skill/SKILL.md`, filed under the playbook it belongs to. Skills that need a specific tool, that invent facts, or that send anything without a person approving it are not accepted.

## License

MIT. See `LICENSE`.
