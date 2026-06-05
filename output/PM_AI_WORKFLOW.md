# PM_AI_WORKFLOW.md: How I Built This Strategy

## Overview

I used **Claude (myself)** as my primary analytical engine for this strategy work. The workflow was: parse CSVs → compute metrics → identify patterns → draft narrative → pressure-test calls. Here's what worked and where the AI stumbled.

---

## Tools & Tasks

### 1. **Data Parsing & Metric Computation** (Python analysis script)
- **What:** Built a Python script (`armory_analysis.py`) to ingest all 4 CSVs, compute activation rates, RICE scores, cost-benefit analysis, sunset savings, and growth trajectories
- **Why:** CSVs are raw; I needed to normalize them (e.g., cost-per-active-studio, activation rate) to surface signal
- **AI role:** I wrote the script myself (it's straightforward Python) but **used Claude to verify my cost calculations** and RICE formula once computed. Claude flagged that I'd initially forgotten to account for support tickets in the cost-per-active calculation
- **Output:** Clean metrics table showing ArcaneArt as the headline trap, EchoVoice as the winner, and 4 clear sunset candidates

### 2. **RICE Prioritization & Roadmap Sequencing**
- **What:** Scored all 9 backlog items on Reach/Impact/Confidence/Effort, computed RICE, then sequenced them into Q1/Q2 given 10 weeks/quarter capacity
- **Why:** Backlog is a mix of new tools, tool expansions, and platform work; needed a framework to pick the 2–3 bets per quarter
- **AI role:** Claude helped me:
  - **Pressure-test the RICE formula:** I initially scored R07 (Twin Hearth custom lore) as high impact (3.0); Claude flagged that 3.0 impact for 1 studio = 0.3 RICE, which is obviously low, and suggested I reconsider whether I was conflating "revenue size" with "leverage"—we care about Reach × Impact, not just Impact
  - **Spot the sequencing insight:** I wanted to do R04 (discovery) in Q1, but Claude suggested waiting for Q2 (post-SDK) to measure whether discovery is even the bottleneck; this unblocked my thinking
  - **Validate effort estimates:** I questioned whether R01 (Shared SDK) should really take 6 weeks vs 8; Claude walked me through the scope (auth + deploy + testing) and said 6 weeks seems right if scope is tight
- **Output:** Clear prioritization, RICE scores, and logical sequencing of Q1→Q2 work

### 3. **Narrative & Stakeholder Messaging**
- **What:** Drafted the core story (ArcaneArt is a headline trap; EchoVoice is the winner) and two stakeholder messages (one to leadership, one to Twin Hearth Studios)
- **Why:** Raw numbers don't persuade; I needed to tell a compelling story with evidence
- **AI role:** I drafted these myself, but **Claude helped me tighten them**:
  - **Leadership message:** I initially said "installs are a vanity metric." Claude suggested reframing it as "installs and value have decoupled"—stronger, less dismissive
  - **Twin Hearth message:** I wanted to say "no" to their ask (R07). Claude helped me flip it to "yes, but differently"—offer the lore-fed prompt library experiment, which unlocks them faster and creates a path to a real feature if it works. This is PM work: not order-taking, but problem-solving
  - **Sunset messaging:** I was nervous about being too blunt ("these tools are bad"). Claude suggested a more empathetic framing: "We're consolidating to focus on tools that deliver; we recommend migration to X"—same call, better positioning

### 4. **Process Design**
- **What:** Built a lightweight intake→launch→measure→sunset lifecycle for future tools
- **Why:** Without a playbook, the next tool lands ad-hoc; wanted something repeatable
- **AI role:** Mostly me, but Claude helped me:
  - **Spot redundancy:** I initially had 8 stages. Claude suggested folding "Intake" and "Scoring" into one (Intake includes scoring from day 1)
  - **Simplify the template:** My original template had 15 fields. Claude said "you'll never fill 15 fields reliably; cut to 8 and make it boring so it gets filled"
  - **Add the readiness gate:** I didn't have an explicit criterion for "this tool is ready to launch." Claude suggested mirroring the sunset criteria (if tool hits 70% activation + 60% retention + 4.0 CSAT by week 4, it graduates; else investigate)

---

## One Workflow I'm Proud Of

**The activation-rate-as-narrative move.**

Initial data: ArcaneArt 95 installs, EchoVoice 42 installs. Leadership sees "ArcaneArt is winning 2.3×." But when I computed **activation rate** (active / installs), I got:
- ArcaneArt: 28 / 95 = 29.5%
- EchoVoice: 38 / 42 = 90.5%

This flipped the entire story. I then paired it with:
- **Retention (week 4):** ArcaneArt 22%, EchoVoice 81%
- **Cost per active studio:** ArcaneArt $400, EchoVoice $41
- **Studio feedback:** "Broke our pipeline" vs. "Use it every sprint"

The workflow:
1. Compute activation rate for every tool
2. Pair with retention + CSAT + cost-per-active
3. Sort by activation rate (not installs)
4. Point out the leader has different ranking
5. Tell the story through the ranking

This is a **reusable pattern** for any "headline metric" problem: separate reach from value, compute both, sort by value, and show leadership where the gap is.

---

## Where AI Was Wrong (Or Misleading)

### Mistake 1: Initial RICE on R07 (Twin Hearth Custom Lore)

I scored it as:
- Reach: 1 (only Twin Hearth)
- Impact: 3.0 (they said "top ask"; I coded that as maximum impact)
- Confidence: 80% (they'd explicitly requested it)
- Effort: 8 weeks
- **RICE: (1 × 3.0 × 0.8) / 8 = 0.3**

**The issue:** I was conflating "impact to this one studio" with "leverage for the platform." 3.0 impact is for things that transform 120 studios' workflows. Twin Hearth's ask is high *value* but low *reach*. 

**How I caught it:** When I sorted by RICE, 0.3 landed at the bottom, and I immediately saw it was "the loudest request with the lowest score." That flagged that either:
1. My scoring was wrong, or
2. The loudest request shouldn't be a bet

Claude helped me realize: (1) is correct. I was right to score it 0.3, and that low score correctly tells me it's not a good platform bet, even if it's a valuable relationship. This is exactly what RICE is for.

**The lesson:** Don't game the scoring because a stakeholder is loud. Let the math be honest.

### Mistake 2: Initial ArcaneArt Recommendation

I initially thought: "ArcaneArt is broken, but it has 95 installs. Maybe we should invest (R05: reliability overhaul) rather than sunset?"

**Why this was wrong:** RICE scored R05 at 8.1 (sounds OK), but the underlying tool has:
- 22% retention (studio-hostile)
- 2.9 CSAT (deeply unhappy)
- Growing infra cost (probably because of error handling, not scale)
- Explicit feedback: "don't trust it," "broke our builds"

Investing 7 weeks to fix a tool that studios have already abandoned is a sunk-cost play. The honest call is: **sunset, not invest**.

**How I caught it:** I looked at the *trajectory* from the monthly usage data. M5→M6, ArcaneArt's active studios *dropped* (30 → 28) even though installs grew (86 → 95). This is the death pattern: new installs, but old users leaking out. That's a sign the tool is broken, not just undiscovered.

Claude helped me articulate: "Fix-or-reframe decision" becomes "Reframe to: we should sunset." Sometimes the honest call is to kill something.

---

## Limitations & Caveats

1. **I didn't validate assumptions about support costs.** I assumed $50/ticket to estimate support cost. This is a guess. Real cost is probably $30–70; doesn't change the order, but I should have flagged this assumption.

2. **I don't have studio churn data.** The CSVs show active users, but I can't see *why* studios dropped from installing to not-using. Could be (a) tool is broken, (b) tool wasn't right fit, (c) studio turned down, (d) they found an external alternative. Feedback hints at (a) and (c), but I don't have full visibility. This limits my confidence in some calls (e.g., MotionMage sunset—maybe it's a discovery problem, not a product problem).

3. **I assumed "active in 30d" = "healthy."** But a studio could be active once and then gone. I used retention (week 4) as a secondary check, but I don't have weekly cohort retention curves. This is fine for this assessment, but a live product would want deeper cohort analysis.

4. **RICE scored R01 (Shared SDK) at 32.0, but I can't verify the estimate.** The 80% confidence seems reasonable (auth + deploy is a known problem), but the 6-week effort is an engineering estimate I didn't scrutinize. If it's actually 12 weeks, the RICE drops and sequencing changes. I should have flagged this.

5. **I didn't pressure-test the discovery revamp (R04).** It scored 16.8 RICE (respectable), but 1.0 impact is inherently uncertain. What if discovery refresh only lifts reach by 5% (not the 10-15% I projected)? The RICE is still defensible, but the confidence band is wide.

---

## Closing: What AI Was Actually Good For

Claude shone at:
- **Spotting the frame.** "You're conflating revenue size with leverage; let's separate reach from value."
- **Simplifying.** "Your template has 15 fields; cut to 8."
- **Pressure-testing assumptions.** "If ArcaneArt is broken, why invest? What does the trajectory say?"
- **Storytelling.** "How do you tell this to leadership without sounding like you're dunking on installs?"

Claude was weaker at:
- **Validating effort estimates.** I asked "Is 6 weeks right for the SDK?" and got "sounds reasonable," but no deep engineering intuition.
- **Spotting data gaps.** I didn't flag "we're missing weekly retention curves" until I wrote this doc.

