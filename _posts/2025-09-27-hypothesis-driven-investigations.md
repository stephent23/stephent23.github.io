---
type: posts
title: "The Power of Hypothesis Driven Investigations"
tags: [Cyber Incident Response, SOC, SOC Analyst, Critical Thinking]
category: Incident Response
toc: true
---

In my last post, [*The Most Important Question Every SOC Analyst Should Be Asking*](https://www.infosecuriosity.co.uk/posts/2025-08-25-the-most-important-question-every-soc-analyst-should-be-asking/), we looked at how analysts should frame alerts and activity by asking: *“So what?”*  

That question is the spark that drives investigation. However, to get from curiosity to conclusion, analysts need a structured way of working through possible answers - this is where hypothesis building comes in.  


## Why Hypotheses Matter  

SOCs are often overwhelmed with noisy, low-fidelity alerts. Clear hypotheses help analysts cut through that noise by bringing structure to investigations and keeping the focus on what’s actually worth pursuing.

- **They provide structure** – Rather than jumping between tools and data sources, hypotheses give analysts a logical path to follow during an investigation.  
- **They reduce bias** – Writing down assumptions forces analysts to question their own thinking, making it less likely they'll settle on the first plausible explanation.
- **They improve efficiency** – A well-formed hypothesis allows analysts to quickly prove or disprove ideas, leading to faster, evidence-based conclusions.
- **They enhance communication** – Documented hypotheses clarify *why* decisions were made, making handovers easier and reducing duplicated work.

In short, hypotheses help SOC teams move from reactive alert chasing to structured, evidence-driven investigations with conclusions that they can be confident in.


## Methods for Building Hypotheses

There are several practical ways analysts can generate useful hypotheses when confronted with alerts, anomalies, or during proactive threat hunting: 

{:.no_toc}
### 1. Alert-Driven Hypotheses 
Start with the alert in front of you and ask:  
*“If this activity is truly malicious, what other activity should I expect to find?”*

- **Example:** A detection fires for suspicious PowerShell usage triggered by an obfuscated command line.
   - **Hypothesis:** An attacker is using PowerShell to download and execute a payload as part of initial access or post-exploitation.
   - **Tests:**
      - Review PowerShell script block logs (Event ID 4104) for indicators like `Invoke-WebRequest`, `Invoke-Expression`, or `DownloadString`.
      - Check Event ID 4688 for related process creation (e.g., PowerShell spawning `cmd.exe`, `mshta.exe`, or `rundll32.exe`).
      - Look for outbound network connections to unfamiliar or suspicious domains/IPs, especially over HTTP/S from PowerShell.
      - Correlate with web proxy or DNS logs to validate external communication attempts.
      - Check for follow-on behaviors, such as the creation of suspicious scheduled tasks, services, or persistence mechanisms.

{:.no_toc}
### 2. Threat-Informed Hypotheses  
Ground detection ideas in established frameworks such as MITRE ATT&CK. This ties hypotheses to real-world adversary behaviour instead of speculation.  

- **Example: Valid Accounts (T1078)**  
  - **Hypothesis:** Successful logins are observed from atypical geographies, irregular hours, or devices not previously associated with the user when adversaries leverage stolen credentials.  
  - **Tests:** Review authentication logs for anomalies in IP address, geolocation, device fingerprinting, or sign-in frequency. Correlate with known travel data and MFA prompts.  

- **Example: Scheduled Task/Job (T1053.005)**  
  - **Hypothesis:** Adversaries attempting persistence through scheduled tasks generate unexpected task creation or modification events in Windows event logs. 
  - **Tests:** Query Windows Event ID 4698 (task creation), looking for tasks created by unusual accounts, binaries in non-standard directories, or unexpected execution schedules. Compare against a baseline of common scheduled tasks in the environment.  

{:.no_toc}
### 3. Adversary Perspective
Adopt a red team mindset and think like a threat actor. What would be your objective? What steps would you take to achieve it?   

- **Example: Compromised Mailbox**  
  - **Hypothesis:** A compromised mailbox would have new inbox rules created, permission changes, or login activity from atypical sources.  
  - **Tests:**  
    - Review Exchange/Office 365 audit logs for:  
      - Creation of forwarding or auto-delete inbox rules.  
      - Delegated mailbox access granted to new accounts.  
      - Logins via legacy protocols.  
    - Correlate mailbox events with authentication logs to confirm consistency with suspicious sign-in activity.

{:.no_toc}
### 4. Hypothesis Trees  
Map multiple plausible explanations for an observation and evaluate each with evidence. This reduces confirmation bias and builds analytical rigor.  

- **Example: Unusual Login Observed**  
  - **Hypotheses:**  
    - A. Legitimate — The user is travelling, and the login is valid.  
    - B. Malicious — Credentials have been compromised and are being actively misused.  
    - C. Technical Artifact — System clock, log source, or SIEM ingestion pipeline is misconfigured, producing misleading timestamps or location data.  

  - **Tests:**  
    - HR/Travel Data - Verify whether the user is known to have travelled to the observed location.  
    - MFA Logs - Check whether MFA challenges were issued and successfully passed.  
    - Log Source Validation - Ensure that logs are using common timezones such as UTC.  
<br> 

By laying out structured, testable hypotheses, analysts avoid tunnel vision and progress toward evidence based conclusions.


## Why Documenting Hypotheses Matters  
Most SOCs already use case management platforms to track alerts and incidents. The real challenge is making sure every hypothesis, even those ultimately disproven, are captured in a way that turns investigative thinking into lasting knowledge rather than disappearing with the case.  

- **Knowledge Sharing**  
  Analysts gain more from understanding *how* conclusions were reached than from outcomes alone. Documented hypotheses preserve the reasoning process, accelerating the development of analytical intuition for new team members.  

- **Auditability and Accountability**  
  Both leadership and compliance stakeholders need transparency. When hypotheses and evidence are recorded together, every decision can be traced back to its rationale, reinforcing confidence in the SOC’s processes.  

- **Continuous Improvement**  
  Recurring hypotheses across investigations reveal common attack patterns. These can be refined into playbooks, codified into detection rules, or automated in workflows, steadily increasing SOC efficiency and maturity.  

- **Bias Reduction**  
  Capturing multiple hypotheses explicitly helps analysts avoid tunnel vision and confirmation bias. Written documentation encourages a more structured, scientific approach to investigations.  



## Closing Thoughts  
If the question *“So what?”* serves as a lens for analysts to critically evaluate investigation results, hypotheses are the vehicle that ensures every investigation is deliberate, efficient, and evidence driven.

For SOCs, embedding hypothesis driven thinking into daily practice cannot be optional — it turns analysts from reactive alert responders into thoughtful investigators capable of understanding not just *what* happened, but also *why* and *how*.

<br>

---

<br>

### Additional Resources for Analysts  

For those wanting to deepen their practice of hypothesis-driven investigations:  

- **MITRE ATT&CK & D3FEND** – map hypotheses to adversary techniques and defensive countermeasures.  
- **SANS DFIR resources** – excellent guides on structured investigations.  
- **David Bianco’s Pyramid of Pain** – useful for hypothesis generation in threat hunting.  
- **Critical thinking literature** – such as Daniel Kahneman’s *Thinking, Fast and Slow* for bias awareness.  