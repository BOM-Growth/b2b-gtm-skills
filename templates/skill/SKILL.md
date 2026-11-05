---
name: my-skill-name
title: My skill name
description: |
  Use this skill when [the concrete trigger: a signal fires, a moment in the quarter,
  a recurring cadence]. Produces [the concrete output]. [One or two more sentences
  dense with the phrases someone would actually say when they need this.]
collection: [playbook slug from playbooks/]
type: play
reads: [1-context/ideal-customer.md, 3-strategy/funnel.md]
related: [another-skill]
playbook: [number]
stage: [foundation | build | distribution | operate]
---

[One line: when this applies. One line: what it produces.]

## Before you start

This skill works on its own. If the person has their own marketing brain (or any folder of context files about their company), read the files listed under `reads` first and cite them for every fact. If they do not have one, do not look for one: ask for the two or three facts this play needs and go on. Never invent a fact.

Tools: [the two or three tools this play usually uses, from TOOLS.md, or the sentence "see TOOLS.md"]. None are required.

## The play

1. Read the context (see Before you start). [What to take from it.]
2. [A GTM verb: "pull the event scans", "check the CRM", "load the ICP gates".]
3. [Next step.]
4. [If a step has depth worth its own page, move it to `references/<topic>.md` and say here when to read it.]

## What good looks like

- [What the best operator notices first that others miss.]
- [The common mistake, what the mediocre version looks like.]
- [How you know the output is good, concretely.]

## Rules

- MUST cite the context file for every fact when a brain exists; say when a fact is missing.
- MUST run `permission-check` before any customer name, quote, logo or number is used.
- NEVER [a hard failure mode].

## Output

[What is returned, in order.] If the person has their own marketing brain, save to [files]. If not, return it as a file they can keep. Do not set up a brain unless they ask.
