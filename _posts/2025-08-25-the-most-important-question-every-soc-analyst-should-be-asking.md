---
type: posts
title: "The Most Important Question Every SOC Analyst Should Be Asking"
tags: [Cyber Incident Response, SOC, SOC Analyst, Critical Thinking]
category: Incident Response
toc: true
---

Security Operations Centres (SOCs) live and breathe questions such as: *What happened? How did it happen? Who is behind it?* But there’s one question that cuts through noise, elevates both analyst effectiveness and organisational resilience, and should sit at the centre of every investigation:  

***“So what?”***

It might sound simple, even dismissive, but it’s the most powerful question an analyst can ask. When asked consistently, it is also the one which most tangibly reduces risk.  


## Why “So What?” Matters  

SOC analysts are often dealing with high volumes of alerts every day *(improving alert fidelity and reducing alert volume is a topic for another post)*. 

Traditional SOC metrics such as “mean time to detect” or “volume of alerts closed” will often drive teams to close as many alerts as possible, as quickly as possible. However, if analysts are not taking the time to ask *“so what?”*, we risk missing essential context and understanding which may determine whether an alert is background noise or a true risk to the business.

- A phishing email that was blocked: *So what?*
: Maybe nothing, or maybe it’s the third blocked attempt against the CFO this week. Perhaps that could indicate a targeted campaign, not just random spam.  

- A standard Windows process making outbound connections to a suspicious IP: *So what?*
: Maybe it’s a misconfigured application, or perhaps a threat actor is leveraging DLL side loading to disguise malicious activity. Perhaps that changes the narrative from “benign anomaly” to “possible command-and-control activity.”  

<br />

*“So what?” isn’t only about the business impact, it’s about understanding the alert itself.*  
- What technique is being used?  
- How does it align to a threat actors objectives?  
- What could happen if it’s ignored?  

By asking *“so what?”* in this broader sense, analysts don’t just close tickets, they uncover the story behind  an alert. This is what enables a SOC to add tangible value and reduce risk to the organisation. 



## Quality over Quantity  

For security leaders, this shift is critical. SOC KPIs often emphasise activity over impact:  
- Incidents handled per analyst
- Mean time to detect/respond
- Volume of alerts closed  

These have value, but they don’t measure whether the SOC actually understands what’s happening. A fast but shallow investigation might leave a threat undetected inside the environment.  

These KPIs should be complemented by tracking **incident quality**, which involves measuring:
- Did the analyst identify what the alert really represented?  
- Was the potential threat path understood, not just the immediate activity?  
- Was the correct containment / eradication actions taken?

When analysts consistently ask *“so what?”* about both the threat and the impact, the quality of investigations improve dramatically.  


## Critical Thinking as a Security Control  

Technology alone cannot answer the question *“so what?”*. Critical thinking should be regarded as a security control in its own right. When analysts adopt this mindset, they are better able to:

1. Understand the nature of the threat  
2. Prioritise responses effectively  
3. Communicate findings with clarity  
4. Refine and tune detections  

The final point is particularly important: asking *“so what?”* serves as a tuning mechanism. If repeated questioning consistently demonstrates that alerts are false or benign positives, that indicates the detection logic requires adjustment. Conversely, if the question uncovers genuine threats, those detections should be prioritised to ensure they receive the appropriate attention in future.


## Hiring for the Right Skills  

This principle should also shape hiring. Too often, SOC recruitment emphasises tool familiarity or certifications. However, tools change rapidly, whereas critical thinking and curiosity do not.  

Analysts who naturally ask *“so what?”* bring more long-term value than those who only know how to operate the latest SIEM or EDR. The best hires are those who can:  

- Break down alerts and explore the “why” behind them.  
- Connect technical observations to adversary TTPs.  
- Translate those observations into understanding and communicating clear business risk.  
- Provide feedback that strengthens the detection and automation pipeline.  

Tools can be taught; mindset is harder to instil. That’s why hiring for critical thinkers should be as important as hiring for technical expertise.  


## A Call to Analysts and Leaders  

If you’re an **analyst**, consciously ask *”so what?”*. Push yourself to understand both the event, how it would fit into the kill chain, the detection logic, the subsequent business risk/impact. 

If you’re a **leader**, adjust KPIs and incentives so your team is rewarded for understanding and investigation quality, not just speed and meeting arbitrary SLAs. When building your SOC, hire for curiosity and analytical rigour - not just tool experience.

<br />

---

<br />
Ultimately, the SOC’s mission isn’t just to close alerts - it’s to reduce organisational risk. That can only be achieved by truly understanding threats and the business, continuously improving detection fidelity and coverage, and ensuring investigations lead to meaningful action. 

The simplest, most powerful path to that mission starts with two words:  

***"So what?"***