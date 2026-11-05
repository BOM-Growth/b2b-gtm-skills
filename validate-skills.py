#!/usr/bin/env python3
"""Checks every skills/*/SKILL.md: frontmatter present with name, description, type, collection; name matches folder;
no em dashes; a Before you start section; collection matches a playbook folder. Exit 1 on any failure."""
import glob, os, re, sys
root = os.path.dirname(os.path.abspath(__file__))
playbooks = {os.path.basename(p)[3:] for p in glob.glob(root + "/playbooks/*/*")}
bad = 0
for p in sorted(glob.glob(root + "/skills/*/SKILL.md")):
    name = os.path.basename(os.path.dirname(p)); t = open(p).read()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    errs = []
    if not m: errs.append("no frontmatter")
    else:
        fm = m.group(1)
        for k in ("name", "description", "type", "collection"):
            if not re.search(rf"^{k}:", fm, re.M): errs.append(f"missing {k}")
        n = re.search(r"^name: (.*)$", fm, re.M)
        if n and n.group(1).strip() != name: errs.append(f"name {n.group(1)} != folder")
        c = re.search(r"^collection: (.*)$", fm, re.M)
        if c and c.group(1).strip() not in playbooks: errs.append(f"unknown collection {c.group(1)}")
    if chr(8212) in t: errs.append("em dash")
    if "## Before you start" not in t: errs.append("no Before you start")
    if errs:
        bad += 1; print(f"{name}: " + "; ".join(errs))
print(f"{len(glob.glob(root + '/skills/*/SKILL.md'))} skills checked, {bad} with problems")
sys.exit(1 if bad else 0)
