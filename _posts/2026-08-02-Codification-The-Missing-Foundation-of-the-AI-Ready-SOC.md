---
type: posts
title: "Codification: The Missing Foundation of the AI-Ready SOC"
description: "Playbooks pose the questions, queries gather the evidence, detections explain why the alert fired, and skills carry the procedure — codification is how you turn analyst expertise into something AI and analysts can both reason over. Part 2 of a series."
tags: [AI, SOC, Security Operations, Cyber Defence, Detection Engineering]
category: Security Operations
toc: true
series: ai-ready-soc
series_part: 2
header:
  og_image: /assets/img/custom/posts/codification-knowledge-base-og.png
  og_image_alt: "The codified knowledge base: playbooks, queries, detections and skills held in version control, applied by investigations run by analysts or AI, with gaps returning as pull requests."
---

*Part 2 of Building the AI-Ready SOC series*

*AI is only as useful as the expertise you give it access to. Codification is how you make expertise accessible.*

In the [first post of this series](https://www.infosecuriosity.co.uk/posts/2026-06-28-Most-SOCs-Are-Thinking-About-AI-the-Wrong-Way/), I argued that the real opportunity of AI in the SOC is not making individual tasks faster, but taking the expertise your best people hold and making it available across the entire SOC operation. That post ended with the harder question: how do we actually capture it?

The answer is codification, and it is less exotic than it sounds. Most teams already have the pieces, although few have been deliberate about bringing them together.

## What We Are Actually Capturing

When a good analyst investigates an incident, they are not working through a checklist; they are asking questions, and interrogating the answers. I have written before about the most important of those questions, [*"so what?"*](https://www.infosecuriosity.co.uk/posts/2025-08-25-the-most-important-question-every-soc-analyst-should-be-asking/), and about how analysts turn that instinct into a [hypothesis driven method](https://www.infosecuriosity.co.uk/posts/2025-09-27-hypothesis-driven-investigations/). That method, the questions and the reasoning behind them, is what we are setting out to capture. Not as prose only a human can interpret, but in a form both analysts and systems can work with.

## The Knowledge Base

Four kinds of knowledge need to be accessible, and they are worth separating because they do different jobs and change at different speeds.

- **Playbooks** pose the questions. Held at the category level, malware, host compromise, credential misuse, data exfiltration, denial of service, rather than per technique or per detection.
- **Queries** gather the evidence. Each retrieves one kind of fact about an entity (e.g. a host, a user, an IP, a mailbox), parameterised so it serves any entity of that type, with an implementation for every platform in your estate.
- **Detections** explain why the alert fired. Detection as code is established practice, for example [Sigma](https://sigmahq.io/), and the benefit here is the context it adds: the logic tells you what behaviour the rule was written to catch and the assumptions behind it. An investigation that starts there is several steps ahead.
- **Skills** are the procedures the AI applies to the work, written once and reused. They hold how an investigation should be run: how the playbooks and queries are used, and how evidence, reasoning and analysis are documented.

Queries deserve a note of their own, because a query is not the answer to a question. "How did this activity begin on the host?" is not one query; it is process lineage, scheduled tasks, service installs and recent logons, weighed together. Nor do queries carry interpretation; what an answer *means* depends on the alert in front of you and the context in which it is asked.

Skills are easily mistaken for playbooks, since both are written down and reviewed. The difference is in what they hold. A playbook holds what to ask, and changes as the threat landscape does; a skill holds how to work, and changes as your standards do. A timeline skill would set out which fields matter, that timestamps are normalised to UTC, and that every entry cites the query it came from. That is what makes two investigations of the same alert read the same way, whoever or whatever ran them.

![The codified knowledge base: playbooks pose the questions, queries gather the evidence, detections explain why the alert fired, and skills describe how the investigation should be orchestrated. All version controlled, one source of truth for analysts and AI.](/assets/img/custom/posts/codification-knowledge-base.svg)

Playbooks and queries connect through the questions themselves. The playbook expresses intent; the query library, where each query records the questions it helps answer, is where that intent is met. A single query often serves several questions, and where none yet exists you have found a gap worth filling.

That is what scales, in both directions. A query written once serves every question that needs it, across every playbook, and a playbook written once covers every detection in its category. Whereas with one automation per detection, every new rule carries its own build and its own maintenance, and the work soon grows faster than you can keep pace with the threat landscape.

## What a Codified Playbook Looks Like

Good playbooks have always led an analyst through questions rather than steps. What changes is how they are written and stored. Machine-readable standards exist, [OASIS CACAO](https://docs.oasis-open.org/cacao/security-playbooks/v2.0/security-playbooks-v2.0.html) among them, but they largely encode workflows to execute: do this, then that. What we are codifying is different: questions to reason through. In practice it can be as simple as this.

```yaml
playbook: host-compromise
analysis:
  initial-access:
    - How did this activity begin on the host?
  execution:
    - Is this consistent with how the host is legitimately administered?
  persistence:
    - Have any scheduled tasks been created or modified?
    - Are there new registry run keys or startup entries?
    - Have any services or WMI subscriptions been added?
  discovery:
    - What did the activity touch, on the host and across the network?
  credential-access:
    - Which identities were involved, and where else were they used?
containment:
  consider: [isolate-host, suspend-account, block-destination]
```

The playbook names no queries; the query library records which questions each query helps answer, because that binding changes far more often than the questions do. Notice too what is absent: no steps, no thresholds, no scripted conclusions. The playbook cannot tell you what an encoded command line means, because on one host it is an intrusion and on another it is how the config management tool has always worked, and reading that is where judgement comes in.

![Category playbooks pose questions; the questions map many-to-many onto a shared query library. One question usually needs several queries, one query serves several questions and several playbooks, and a question with no query behind it is a gap worth filling.](/assets/img/custom/posts/questions-are-the-common-language.svg)

A real playbook runs longer than this, and carries the eradication, recovery and post-incident questions too. Two things evolve from there, and they feed each other. The knowledge base grows as questions are added, queries extended and skills refined, and the autonomy you grant grows with it. Early on that might be triage only, with an analyst reviewing before anything is closed and containment suggested rather than taken; as confidence builds, you widen what an AI agent is trusted to do on its own.

## Whose Questions Should the AI Be Asking?

It is a fair challenge that a capable model can generate its own questions and does not need your playbook at all. It will often produce good ones, sometimes better than yours, and we should not constrain that.

However, we can view the playbook as a floor rather than a ceiling. It sets out the questions that should always be asked within the context of your organisation, and beyond that the model can still reason freely. Nor is it fixed. Analysts will add and revise questions as the threat landscape shifts, and where the model keeps reaching for a question the playbook does not contain, that is a signal too: it becomes a pull request, and the baseline improves.

It is telling that the platforms marketed as not requiring playbooks still describe themselves as mimicking expert analyst reasoning and applying customer context to every investigation. I have yet to see anyone running models without codified knowledge behind them; the disagreement is only over who writes it, and whether you can review it.

The same challenge applies to the queries. There, the difference is that a reviewed query is known to be correct for your schema and platforms. A generated one may quietly search the wrong table or field, and an empty result that looks like nothing found is worse than no answer at all, because it closes a line of enquiry with false confidence.

## Version Control Is Not Optional

Where this knowledge lives matters almost as much as its shape. Tools such as Git enable you to inherit an entire quality system for free.

- **Review before release.** A change goes through a pull request, scrutinised by another analyst exactly as an engineer reviews code. A question nobody can justify does not survive.
- **Testing before trust.** Queries can be validated in CI against your schema and platforms, so when a log source changes shape the query fails loudly in the pipeline instead of silently returning nothing in an investigation. This is not theoretical; Elastic's public [detection rules repository](https://github.com/elastic/detection-rules) runs schema validation and unit tests over its rules in exactly this way.
- **History and accountability.** Every change is attributed and reversible, providing greater auditability.

None of this guarantees the knowledge base stays current, and a repository nobody contributes to will go stale, exactly like a wiki nobody edits. The difference is that the neglect is visible. Every question and query has an author and a date behind it, so anything untouched for a year is easy to find and easy to challenge.

## You Are Further Along Than You Think

This can sound like a mountain of work, but often it is smaller than it looks, because much of the material already exists. Your detections encode what you think is worth alerting on, your existing playbooks sketch your common categories, your closed cases record which questions actually resolved them, and your best analysts already have their favourite queries saved in personal notes and pasted between tickets. Codification is mostly gathering, structuring and reviewing what is already there.

Start where the volume is. Take your highest volume alert category, sit with your strongest analysts, capture the questions they actually work through, and put one playbook and its handful of queries through review. AI can help here too, reading back through resolved tickets to surface the questions and queries that actually moved those investigations forward. That single exercise will teach you more about the shape of your knowledge than any amount of planning.

## Closing Thoughts

Codification is the unglamorous middle of this series, and the part everything else depends on. Start building the knowledge base and you have a reference your analysts can rely on, and a foundation an AI can reason over.

Which raises the question I have been circling since the first post. If the expertise is codified and the machines can apply it, what is left for the analyst? A lot, as it turns out, and that is the next post. The platform that brings it all together, and the guardrails it needs, will follow after.
