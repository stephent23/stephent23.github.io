---
type: posts
title: "The Future SOC Analyst: Directing the Known, Investigating the Novel"
description: "As AI takes over routine investigation, the SOC analyst directs the AI, investigates the novel and leads incidents, and developing people for that role needs deliberate design. Part 3 of a series."
tags: [AI, SOC, Security Operations, Cyber Defence, Critical Thinking]
category: Security Operations
toc: true
series: ai-ready-soc
series_part: 3
---

*Part 3 of Building the AI-Ready SOC series*

*As AI takes on more of the investigative work, the analyst's role changes, and so does the way we develop analysts.*

In the [previous post](https://www.infosecuriosity.co.uk/posts/2026-08-02-Codification-The-Missing-Foundation-of-the-AI-Ready-SOC/), I covered codifying the knowledge behind an investigation: playbooks that pose the questions, queries that answer them, skills that capture the know-how, and detections that explain the alerts. Once that knowledge is in place and AI can apply it, the next question is what the analyst does.

The role changes, and in many ways for the better. Developing people into that role will need more thought.

## What AI Takes On

In the first post I split the work three ways. Automation handles the certain, AI handles the variable, and people handle the novel.

AI can now do much of the repetitive investigative work in a SOC. It works through the same questions on high-volume alert categories, pulls the evidence, summarises what it found and documents it, at any hour and with the same consistency every time. This is already happening, and the Tier 1 role will change as a result. The analyst keeps the third job, and it comes in three parts.

## Directing the Known

For the work AI does well, the analyst directs it. Take a PowerShell alert. The AI works through the playbook questions, decodes the command, sees that the parent process is a software deployment tool and recommends closing the alert as benign. The analyst reviewing the investigation notices that nobody asked whether that tool had ever launched encoded PowerShell on this host before. A query shows it had not, so the alert is escalated, and the new question goes into the playbook through a pull request.

That one case covers most of the directing role:

- Checking the reasoning, the way a senior analyst reads a junior's work. Is the evidence sound, were the right questions asked, does the conclusion follow?
- Feeding what they learn back into the queries, playbook questions and detections, through the same review process described in the last post.
- Owning the decision. What a finding means for the business, how much risk it carries, whether to contain a host or block a domain. The playbook offers options and a person decides. If an AI investigation is wrong and someone signed it off, that person is accountable, so decide up front who signs off and what they are expected to have checked.

Checking the reasoning needs particular care. [Research on automation in SOCs](https://doi.org/10.3390/computers13070165) describes automation bias and complacency, where analysts rely on automated results and stop looking for evidence that contradicts them. That work predates AI-led investigation, but a fluent, confident write-up is easy to accept, so the risk is likely to carry over. Verification needs to be built into the process.

## Doing the Novel

Directing is only part of the role. Reviewing AI output all day would be dull work and a waste of experienced people.

The rest of the analyst's time goes to work that has no playbook yet: hunting, investigating activity nobody anticipated, and working out what a new technique means for the detections you have. Much of what frontier AI does today is find existing weaknesses faster. As models improve, the line between known and novel will keep moving, and whatever falls on the novel side of it belongs to the analyst. That is where human judgement matters most, and where threat intelligence earns its place. When an analyst finds something new, they write it up as a detection or a playbook question, and the next occurrence is handled by AI. The novel work is also what keeps senior analysts engaged, so protect time for it.

## Leading the Response

When an alert becomes an incident, the work stops being mainly technical. AI can draft the timeline and summarise the evidence. The analyst decides what to contain and when, briefs leadership, works with IT, legal and communications, and keeps the whole response coordinated. Analysts who run incidents connect the technical picture to the business decisions that follow, and that is some of the most important work in the SOC. It is learned by doing, which makes it another reason to design development carefully.

All of this depends on the same thing: knowing what a sound investigation looks like. A conductor knows every instrument well enough to hear when one is off.

## Where Do Senior Analysts Come From?

Being hands-on is how most of us built that knowledge: triaging alerts, learning what normal looks like, seeing how false positives behave and how attacks unfold.

If AI takes on that work and nothing else changes, junior analysts are asked to supervise a system before they have the experience to challenge it.
Hands-on experience can no longer be relied on to build these skills, so development needs to be structured and deliberate. There is an upside, because a junior analyst can see how a senior thinks much earlier than before. Five things help:

- Read the reasoning. A good AI investigation shows its working: the questions asked, the queries run and the evidence behind the conclusion. A junior learns from seeing how the conclusion was reached.
- Investigate first, then compare. On a sample of cases, juniors work the investigation themselves, then review the AI's version and document where and why they differ.
- Contribute to the knowledge base. Writing a playbook question or a query requires understanding it, and a senior reviewing the pull request is mentoring.
- Shadow real incidents. Incident coordination is learned by watching it done, so put juniors on the call as scribe or observer.
- Keep the seats. A SOC that stops hiring juniors is borrowing against its future senior bench. A senior hire costs more, takes months to find and arrives without your environment's context. Growing one takes years, so the decision to stop hiring juniors is made long before its cost shows up. Use some of the efficiency gains to fund structured development.

## Closing Thoughts

The analyst of the future has a higher bar to meet: checking AI's reasoning, investigating what nobody has seen before and shaping the knowledge AI works from. That judgement is built through experience, so how we grow people into it is a design decision for leaders. We owe that to the analysts who are just starting out.

With the knowledge codified and the people developing, the remaining question is the platform: how it brings everything together safely across every tool you run, and what it costs. That is the final post in the series.