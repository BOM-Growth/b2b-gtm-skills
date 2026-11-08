# AI-native GTM ops

Status: draft
Playbook 17 of 19. Stage: Operate. This is the layer every other playbook runs on. It has no skill of its own in this repo because it is the practice of using the other skills well.

## What it produces

A go-to-market team that runs the playbooks with AI assistants doing the drafting, the filing and the first pass of the analysis, with a person deciding and a person approving anything a customer will see.

## Why it matters

The assets a go-to-market function needs (positioning, pages, sequences, decks, reports, lists) used to take a team weeks. With a marketing brain for context and a skill for each job, one person with an assistant produces them in hours and keeps them consistent. The risk is the same speed applied to generic context: fast, confident and wrong. The brain and the human in the loop are what prevent that.

## Order of operations

1. Start with the marketing brain. Every skill reads it when it exists; without it the assistant is guessing.
2. Install the skills from this repo into whichever assistant the team uses (Claude, Claude Code, Codex, or paste the SKILL.md). Run one skill at a time; each works on its own.
3. Connect the tools the skills recommend only where it saves real time: the CRM, the call recorder, the document store, the ad accounts. Read access first. Write access only with an approval step.
4. Set the rules: the assistant drafts, a person approves; the assistant files, a person reviews the file once a week; nothing goes to a customer, a prospect or the public without a person reading it; no facts about the business are invented, a blank is a question.
5. After every meeting, file to the brain. After every skill run, save the output where the skill says.
6. Once a month, read the foundation files for drift, and ask the team which repeated task should become the next skill. Write it in the same format as the ones here.
7. Give the team time on the clock to try new tools, one specific use case per person, and share what worked.

## Who is involved

The go-to-market lead owns the brain and the rules. Everyone on the team runs skills for their own work. The founder sets the approval rules.

## How long it takes

A day to install and set rules. Ten minutes a day to file. The gains compound from month two.

## Signs it needs revisiting

- Output is generic: the brain is thin or not being read.
- Something went to a customer without a person reading it.
- The same manual task is being done every week with no skill for it.

## Skills in this playbook

No skill of its own. The loops listed under Marketing brain, Content and proof, Events and Measurement and reporting are the practice; `marketing-brain` is the foundation. To write a new skill, copy the shape of any SKILL.md in `skills/`.
