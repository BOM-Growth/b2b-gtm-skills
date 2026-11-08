---
name: marketing-brain
description: Set up and maintain a marketing brain, a folder of plain text files about a business that an AI assistant reads before doing any marketing work. Use when starting the brain, when the user pastes a transcript, email, note or decision to be filed, or before any marketing task so the assistant has context.
title: Marketing brain
collection: marketing-brain
type: play
playbook: 2
stage: foundation
---

# Marketing brain

Goal: the AI stops asking "tell me about your business" and stops producing generic output. Everything it needs lives in one folder of plain text files. Humans edit them. The AI reads and updates them. Every meeting, email and decision makes the next piece of work better.

## Before you start

This skill works on its own and is the only one in the repo that creates a brain. Run it when the person asks for one, or when they say yes to the one-line offer another skill makes. Tools: a folder in Google Drive, OneDrive, SharePoint or a repo; nothing else is needed.

## The folder

```
marketing-brain/
├── README.md index for humans: what is here and how to use it
├── CLAUDE.md instructions for the AI: read this folder first
├── 1-context/ who you are
│ ├── company.md
│ ├── ideal-customer.md
│ ├── personas.md
│ ├── offers.md
│ ├── competitors.md
│ └── stack.md which tool holds which record
├── 2-standards/ how you sound and what you may claim
│ ├── brand-voice.md
│ ├── terminology.md
│ └── proof-rules.md
├── 3-strategy/ where you are going
│ ├── goals.md
│ ├── positioning.md
│ ├── messaging.md
│ └── funnel.md stage definitions and attribution rules
├── 4-playbooks/ how you do things
│ ├── content.md
│ ├── outreach.md
│ └── crm-setup.md
├── 5-current/ what is happening now
│ ├── priorities.md
│ ├── calendar.md
│ └── decisions-log.md
└── sources/ raw material, never edited
 ├── transcripts/
 ├── emails/
 └── notes/
```

Where to keep it: a folder in Google Drive, OneDrive or SharePoint is fine. Plain text or Google Docs both work. The AI only needs to be able to read the files. People who already use GitHub can keep it in a repo, but that is optional and most businesses do not need it. A ready-made empty copy of this folder is in this repo as `marketing-brain-template/`; copy it into your Drive to start.

Rules for the folders:
- Folders 1 to 4 hold things that stay true for months. Folder 5 holds things that change weekly.
- `sources/` is where raw material goes exactly as received. The AI reads from it and writes summaries into the numbered folders. It never edits a source.
- Dated or temporary information always goes in `5-current/`, never in `1-context/` or `3-strategy/`.

## Mode 1: set up the brain

Run this when the folder does not exist yet.

1. Create the folder structure above. Every `.md` file starts with a one-line heading and the line "Status: draft" until the person confirms it.
2. Write `CLAUDE.md` with these instructions: "Before any marketing task, read README.md, then 1-context/, 2-standards/ and 3-strategy/. Treat 5-current/ as the latest status. Never invent facts about the business; if a file is missing information, ask. When the user shares a transcript, email, note or decision, file it using the marketing-brain skill."
3. Write `README.md`: what each folder is for in one line each, and how to add to it.
4. Take the first pass yourself. Do not start with blank files and do not start with an interview. Use everything you already know about this business from this conversation, from earlier conversations, from their website if you can read it, and from anything they have pasted. Write a first draft of every file in folders 1 to 4. Mark every line you are unsure of with "(check)". Mark every line you had no information for with "(unknown)". Never invent facts to fill a gap.
5. Show the person the drafts one folder at a time and ask them to correct what is wrong and fill in the unknowns. Five minutes per folder is enough. Remove the "(check)" marks as they confirm lines.
6. If they have already run the positioning-one-liner skill, put the result in `3-strategy/positioning.md`.
7. Tell the person: feed it after every meeting. Paste in the transcript or your notes and say "file this".

## Mode 2: file something

Run this when the person pastes or points to a transcript, email, message, note, or says "we decided X".

1. Save the raw material unchanged in the right `sources/` subfolder with a date in the filename, for example `sources/transcripts/2026-03-14-call-with-supplier.md`.
2. Read it and pull out only what is durable:
 - A fact about the company, customer, offer, or a competitor → the matching file in `1-context/`
 - A phrase the person uses, or a term the customer uses → `2-standards/`
 - A goal, a positioning change, a message that worked → `3-strategy/`
 - A step-by-step way of doing something → `4-playbooks/`
 - A decision, a deadline, a priority, a status → `5-current/`
3. Update each file. Add new lines; change a line only when the new information supersedes it, and keep a short note of what changed and when ("was X until March 2026"). Never delete history.
4. Add one line to `5-current/decisions-log.md` for every decision, with the date and the reason.
5. Report back in five lines or fewer: what was filed where, and anything that contradicted an existing file so the person can resolve it.

## Mode 3: use the brain

Before any marketing task (a post, a page, an email, a competitor comparison, a CRM setup, anything), read `README.md`, `1-context/`, `2-standards/`, `3-strategy/`, and the relevant playbook. Then do the task. Cite which files informed it. If a file was empty or marked draft and that mattered, say so.

## Rules

- Never invent facts about the business. A blank file is a question for the person, not a gap to fill creatively.
- Plain language in every file. A new employee should understand them on day one. No internal jargon without a definition in `terminology.md`.
- Keep files short. If a file passes two screens, split it.
- The person owns the files. Always show what will change before overwriting anything they wrote.
