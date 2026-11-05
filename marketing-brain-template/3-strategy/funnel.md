# Funnel definitions
Status: draft

The stage definitions every reporting, routing and experiment skill reads. One definition per stage, measured in one place. If two tools disagree, the system of record named here wins.

## Stages

| Stage | Definition | Measured in | Owner |
|---|---|---|---|
| Visit | A session on the marketing site | [web analytics] | Marketing |
| Lead | A known person with a captured source | [CRM] | Marketing |
| MQL | [e.g. a demo request, an event scan, a referral intro] | [CRM] | Marketing |
| SQL | Sales-accepted and inside the ICP gates | [CRM] | Sales |
| SAL | [e.g. a demo or discovery held] | [CRM] | Sales |
| Opportunity | A deal with an amount and a stage | [CRM] | Sales |
| Closed won | Signed | [CRM] | Sales |

## What marketing is measured on

Opportunity creation: Lead, MQL, SQL and SAL volume by channel. Closed won is a sales number and does not belong in marketing reporting.

## Conversion definitions by channel

Paid channels count different things as a conversion. Align every channel to one event before comparing them.

| Channel | What the platform calls a conversion | What we count | Note |
|---|---|---|---|
| Paid search | [platform conversion] | Demo request | |
| Paid social | [platform conversion, often a page visit] | Demo request | Platform numbers are not comparable until aligned |
| Events | Badge scan | MQL; SQL when flagged on site | |
| Referral | Intro email sent | MQL; SQL at demo | |

## Attribution rules

- One first-touch source per lead.
- A form submission beats a phone call for attribution when both exist.
- Event leads carry the event name as the source.
- [Any tracking gaps and their status]
