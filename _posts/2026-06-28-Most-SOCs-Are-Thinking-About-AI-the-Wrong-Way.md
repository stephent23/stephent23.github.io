---
## type: posts
title: Most SOCs Are Thinking About AI the Wrong Way
tags: [AI, SOC, Security Operations, Cyber Defence]
category: Security Operations
toc: true
---

*Part 1 of Building the AI-Ready SOC series*

*The real opportunity is not faster alerts. It is scaling the expertise your best people already have.*

![The three jobs in the AI-ready SOC: automation handles the certain, AI handles the variable, people handle the novel, along a spectrum from certain to novel.](/assets/img/custom/posts/three-jobs-ai-ready-soc.svg)

Every vendor has an AI story, every security leader is being asked for an AI strategy, and most of the discussion when it comes to the SOC, circles the same handful of questions. Can AI triage alerts faster? Can it help with investigations? Can it write detections?

Plenty of SOCs will tell you they are already using AI. It might be embedded in the controls they monitor, or analysts might be using prompt features to help understand and document investigations. Useful as that is, it tends to be disjointed, and it addresses a very small part of the SOC problem.

The common thread is that AI is being bolted onto tasks we already do, one at a time. It makes those tasks a little faster, but it leaves the shape of the work untouched. The bigger opportunity is to take the expertise your best people hold, combine it with the context inside your own environment, and make it available across the whole operation. It is a far more fundamental shift than making any single task faster.

## The Problem Is Speed, Not Just Volume

Every security team knows the feeling of being overwhelmed by alerts and the threat landscape is now moving faster than we can keep up with.

We already know where this is heading. Frontier AI models will let adversaries move quicker, automating reconnaissance, chaining exploits together, and taking advantage of exposed attack surface faster than before. They will also lower the barrier to entry for less capable actors. The same capability that can help us defend, is just as available to the people we are defending against.

That leaves defenders with a dual challenge. We have to scale our own capability while facing adversaries whose capability is itself becoming more scalable. The traditional answers help, but only so far. Hiring is slow and good people are scarce. Outsourcing buys coverage, not knowledge of your environment. More tooling brings more noise. All of them scale *activity*. None of them scale *expertise*, and expertise is exactly what the pace of the modern threat landscape demands.

## Three Jobs We Keep Confusing

Before going further, it is worth being clear about the different kinds of work a SOC actually does. I was always a firm believer that automation would not replace analysts, and I think the same is true of AI. That does not result in nothing changing but means that we need to be deliberate about the role each one plays.

- **Automation handles the certain.** Known steps, predictable outcome: enrichment, ticket creation, blocking a known-bad indicator. Fast, reliable, cheap.
- **AI handles the variable.** Choosing and running the right investigative steps for the situation in front of it, then making sense of what comes back.
- **People handle the novel.** Genuinely new attacker behaviour, ambiguity, business judgement, and deciding what gets captured for AI to use next.

Automation is not going anywhere; it keeps doing the certain work it has always done well. AI is what lets us take on the variable, reasoning through a situation rather than following a fixed set of steps. What it will not do is handle the novel, and that is why analysts remain critical. They are also what makes the AI and automation effective in the first place.


## Why We Cannot Automate Our Way Out

Traditional automation is built around detections. A detection fires, a playbook runs. The playbook is hand-built, tied to that specific detection, and maintained by someone on the team. This works well enough for broad, well-understood techniques where the steps rarely change.

It struggles in two situations:

- **Ambiguity.** Plenty of activity, living off the land being the obvious example, is indistinguishable from legitimate use on the surface. The deciding factor is the context around it, not the event itself, and a fixed playbook has no way to weigh that.
- **Volume.** Keeping up with a fast-moving threat landscape means more detections all the time, and hand-building a bespoke automation for every one of them does not scale. There are not enough hours, or analysts, to win that race.

## Codify Once, Apply Everywhere

Codification means capturing an analyst’s expertise once, in a form something else can use, rather than re-running it by hand or hard-wiring it into a playbook for a single alert.

Take a PowerShell process flagging on a host, the kind of living off the land activity automation struggles with. A good analyst does not follow a fixed script. They work through a set of questions. What is the full command line, and is it encoded or obfuscated? What launched it, an Office document, a scheduled task, something else? Is it reaching out to the network, and to where? Each question has a query behind it, and the answers point to the next thing worth investigating. Capture those questions, the queries that answer them, and what they connect to, and the same line of investigation can be applied to every similar alert, not only when that analyst is on shift.

This is the part automation never managed; it could execute fixed steps, but not the reasoning behind them. An analyst could reason through any one of these alerts themselves. What they cannot do is reason through all of them, fast enough, every time. That is what codified expertise applied by AI makes possible.

That is the real shift. Not AI doing the work instead of your experts, but their expertise applied at a scale they could never reach alone. How you actually capture it is the harder question, and it is where this series goes next.

## AI Is Only as Good as What It Can See

A capable model is no longer the challenge, the bigger constraint is what the AI can actually reach.

Most AI built into security products only sees its own platform. The AI in a Network Detection and Response (NDR) tool sees network data, and nothing else. Yet a real investigation rarely stays in one place. To work out what a suspicious connection means, you need the endpoint it came from and the identity behind it. An analyst would never try to reach a conclusion from the network alone, and an AI confined to a single control is under the same limitation.

To be genuinely useful, AI has to work across controls the way an analyst does, following the investigation wherever it leads rather than stopping at the edge of one tool. An AI that sees one layer is a useful feature but it is not an investigative capability.

## Closing Thoughts

The future SOC will not be defined by how much AI it buys, but by how well it turns human expertise into something AI can apply at scale. Get that right and AI becomes a real multiplier. Get it wrong and you have bought an expensive way of doing exactly what you did before. For those leading security, the prize is not efficiency for its own sake but resilience: covering more ground, more consistently, without burning out the few people who can do the hardest work.

None of this removes the need for good analysts. It changes what they spend their time on, shifting them from routine triage towards the judgement and novel problems that AI cannot reach. That is a bigger change to the role than it first appears, and one I will come back to later in the series.

If expertise is the asset, the obvious next question is how we capture it. The encouraging part is that the raw materials already exist, sitting in your runbooks, your detections, and the heads of your best analysts. They are simply not yet in a form AI can use. That is where the next post will go.
