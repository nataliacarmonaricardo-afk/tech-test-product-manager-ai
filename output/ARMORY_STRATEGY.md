# The Armory Storefront: 2-Quarter Strategy

**For:** Head of Product | **Time to read:** 12–15 minutes

---

## 1. Storefront Diagnosis & Success Metrics

**The headline trap:** ArcaneArt has 95 installs (highest), but only 28 active studios (29.5% activation), 22% retention, 2.9 CSAT, and costs $11,200/month. Leadership sees 95 and thinks "winning"; the ground truth is 67 abandoned installs and a broken product.

**The real winner:** EchoVoice—42 installs, 38 active (90.5% activation), 81% retention, 4.7 CSAT, $1,550/month. Studios say: "Use it every sprint, saved us weeks." 10× more efficient than ArcaneArt.

**The gap:**

| Metric | ArcaneArt | EchoVoice | BugHound (beta) |
|--------|-----------|-----------|-----------------|
| **Activation** | 29.5% | 90.5% | 88.9% |
| **Retention (W4)** | 22% | 81% | 78% |
| **CSAT** | 2.9 | 4.7 | 4.6 |
| **Cost/active studio** | $400 | $41 | $50 |

**This separation of reach from value is the entire story.** ArcaneArt looks big (95 installs) but bleeds studios and money. EchoVoice looks small (42 installs) but delivers real value—sticky, efficient, and loved.

**Platform snapshot:** 477 installs, 223 active studios (46.8% overall activation). We're leaving 55% of value on the table due to install→activate friction. Studios report: "Every tool has its own login—setup takes a day" and "Can't tell which tools are new."

**North-star metric:** **30-day active studios** (not installs—installs don't drive value or retention).

**Supporting metrics:**
- **Activation rate** (installs→30d active): Target 70%+
- **Retention (W4):** Target 70%+
- **CSAT:** Target 4.0+
- **Cost/active studio:** Target <$50

Stop reporting installs. They're marketing output, not product health.

---

## 2. Adoption Plan: Install → Active

**The blocker:** Platform friction (setup, discovery, onboarding)—not tool quality.

**Pick 1–2 tools to grow first:** EchoVoice (proven, studios asking for expansion) and BugHound (beta with top-tier metrics, ready to graduate).

### Concrete moves:

**Q1: Shared deploy + auth SDK (6 weeks)**
- Single login + one-click install→authenticate→deploy across all tools
- Removes the day-long setup tax
- Impact: +15–20% activation platform-wide

**Q1 (parallel): EchoVoice multi-language (4 weeks)**
- Studios explicitly ask: "Our players are global"
- Proven tool + explicit demand = high-confidence bet
- Impact: +15–20% activation from non-English studios

**Q2: Storefront discovery revamp (5 weeks)**
- Add filters, highlight "new" tools, recommend based on existing installs
- Impact: +10–15% reach for newer tools (we're burying BugHound behind older ones)
- Run this after SDK so you have data on what friction remains

**Measurement:** Track activation rate weekly by tool. **If these moves hit target, we reach 70% platform activation by Q2 end (from 46.8% now)—that's 70+ new active studios.** Target: 70% platform activation by end of Q2.

---

## 3. Readiness Calls: Launch / Invest / Sunset

**Criteria** (tool must pass all three to stay live or launch):
1. **Activation:** ≥70% of installs active in 30d
2. **Retention:** ≥60% of active studios return in week 4
3. **Satisfaction:** CSAT ≥4.0

**Invest if:** All three criteria met + explicit studio demand exists.

**Sunset if:** 6+ months live + (Activation <40% OR Retention <35% OR CSAT <3.5).

---

### Q2 Immediate Calls

**🚀 Launch:** BugHound (beta → live)
- Meets all criteria: 88.9% activation, 78% retention, 4.6 CSAT
- Waitlist demand for CI/CD integration (explicit in feedback)
- Ready to go

**💪 Invest:** EchoVoice
- Proven winner; multi-language is the natural expansion
- Studios want it; high confidence (90%)

**🗑️ Sunset:** ArcaneArt, MotionMage, TileMancer, QuestGen
- All fail readiness criteria (retention <35% or CSAT <3.5)

| Tool | Active | Retention | CSAT | Cost/mo | Savings |
|------|--------|-----------|------|---------|---------|
| ArcaneArt | 28 | 22% | 2.9 | $11,200 | $11,200 |
| MotionMage | 4 | 18% | 3.1 | $2,450 | $2,450 |
| TileMancer | 6 | 19% | 3.0 | $2,200 | $2,200 |
| QuestGen | 2 | 12% | 2.8 | $800 | $800 |
| **TOTAL** | **40** | — | — | — | **$16,650/mo** |

**The math is simple:** These 4 tools collectively cost $16,650/month and serve only 40 unhappy studios. The feedback confirms frustration (broken updates, never worked for their use case, feels abandoned). Sunsetting them frees capacity and removes the support drain.

**Messaging:** "We're consolidating to focus on tools that deliver. ArcaneArt sunset June 30; we recommend [migration path]." Minimal studio impact (only 40 combined active; feedback shows they're already frustrated).

---

## 4. 2-Quarter Roadmap (RICE-Scored)

**Framework:** (Reach × Impact × Confidence) / Effort

**All 9 backlog items, ranked:**

| Rank | Request | RICE | Reach | Impact | Conf | Effort | Notes |
|------|---------|------|-------|--------|------|--------|-------|
| 1 | R01: Shared SDK | **32.0** | 120 | 2.0 | 80% | 6w | Unblocks all tools |
| 2 | R02: EchoVoice multi-lang | **18.9** | 42 | 2.0 | 90% | 4w | Proven winner + demand |
| 3 | R03: BugHound GA + CI/CD | **16.8** | 60 | 2.0 | 70% | 5w | Beta graduation |
| 4 | R04: Discovery revamp | **16.8** | 120 | 1.0 | 70% | 5w | Unlocks reach |
| — | R05: ArcaneArt fix | 8.1 | 95 | 1.0 | 60% | 7w | **Skip: sunset instead** |
| — | R07: Twin Hearth bespoke lore | **0.3** | 1 | 3.0 | 80% | 8w | **Skip: 1-studio reach** |
| — | R06: ShaderSmith (new) | 2.2 | 35 | 1.0 | 50% | 8w | Unvalidated |
| — | R09: CutsceneDirector (new) | 2.0 | 25 | 2.0 | 40% | 10w | Too risky |
| — | R08: Analytics dashboard | 12.0 | 120 | 0.5 | 80% | 4w | Nice-to-have |

---

### Q1 Plan (10-week capacity)
- **R01 (Shared SDK): 6 weeks** — Foundational; unblocks every tool
- **R02 (EchoVoice multi-lang): 4 weeks** — Parallel; proven bet

**Why:** SDK removes platform friction (the #1 blocker). EchoVoice expansion captures demand on the tool that's already working best.

### Q2 Plan (10-week capacity)
- **R03 (BugHound GA + CI/CD): 5 weeks** — Graduates beta with SDK live
- **R04 (Discovery revamp): 5 weeks** — Data-informed after 6 weeks of SDK + EchoVoice results

**Why:** SDK live makes BugHound GA stronger. Discovery changes are informed by SDK impact data.

### Deprioritized
- **R05 (ArcaneArt fix):** Don't invest 7 weeks in a 22%-retention product. Sunset instead.
- **R07 (Twin Hearth custom lore):** RICE 0.3; only reaches 1 studio. See stakeholder section.
- **R06, R09 (New tools):** Unvalidated and expensive. Queue for Q3.
- **R08 (Analytics):** Low impact (0.5). Defer to Q3.

---

## 5. Stakeholder Alignment

### Message to Leadership

We've grown to 477 installs (healthy). But **installs and value have decoupled**. Our highest-install tool (ArcaneArt, 95) is our biggest failure: 22% retention, $11.2k/month cost, studios say it "breaks our pipeline."

**Real metric:** 223 active studios (46.8% activation). Clear winners (EchoVoice, 90% activation, 4.7 CSAT) and clear losses (4 tools costing $16.6k/month, <40 active studios total).

**Goal shift:** From "double down on installs" → **"Hit 70% platform activation + cut cost-per-active from $60 to $40 in 2 quarters."**

**How:** (1) Fix install→activate friction (shared SDK), (2) invest in proven winners (EchoVoice multi-lang, BugHound GA), (3) sunset bottom 4 tools.

**Result:** 35% more active studios, 50% lower cost. Installs will follow.

---

### Message to Twin Hearth Studios (re: Custom Lore Fine-Tune Request)

Your ask for a bespoke LoreWeaver fine-tuned on Hollow Crown lore is ambitious. Here's our honest math: **8 weeks of engineering for 1 studio**—we can't justify this as a platform bet, and a one-off bespoke build isn't repeatable.

**What we can do faster:** You're already using EchoVoice successfully ("Use it every sprint"). We're shipping multi-language VO in Q1 (4 weeks, ready March). LoreWeaver is solid for you (4.2 CSAT); the gap is domain knowledge, not a new model.

**Our proposal:** Q1 experiment—bundle LoreWeaver + lore-fed prompt library + monthly check-ins with your writing team. Low effort, fast iteration. You ship faster than waiting for custom code. If this unlocks major value, we fund the fine-tuning as a general feature in H2.

This unblocks you in weeks, not months, and doesn't sideline our roadmap. You're important to us, and this shows it.

---

## 6. Intake-to-Launch Process

| Stage | Timing | Owner | Output |
|-------|--------|-------|--------|
| **Intake** | Ongoing | Studios + teams | Request card |
| **Scoring** | Monthly | PM + Head of Eng | RICE scores; updated backlog |
| **Prioritization** | Quarterly | PM + Head of Product + Head of Eng | Top 2–3 bets + rationale |
| **Build** | Quarterly sprint | PM + Tool team | Shipped feature/tool |
| **Launch** | End of quarter | PM + Support | Announcements; day-1 support |
| **Measure** | Weeks 1–4 | PM | Activation, retention, CSAT |
| **Iterate/Sunset** | Week 4+ | PM + Head of Product | Keep live, invest, or sunset |

**Request Card Template:**
```
Title: [Concise]
Type: New tool | Tool expansion | Platform feature
Source: Studio feedback | Internal idea | Market research
Reach: [# studios]
Impact: [0.25–3.0 + rationale]
Confidence: [%]
Effort: [Person-weeks]
One-liner: Why this matters
```

**Readiness Gate:** Does tool hit **70% activation + 60% retention + 4.0 CSAT by week 4?**
- **Yes** → Stay live. Plan expansion bets.
- **No** → Root-cause analysis. Fix, pivot, or sunset with 30-day notice + migration path.

---

## Summary

| Item | Action | Impact |
|------|--------|--------|
| **Sunset 4 tools** | ArcaneArt, MotionMage, TileMancer, QuestGen | Save $16.6k/mo |
| **Launch BugHound** | Graduate from beta (Q2) | +1 proven tool at 88% activation |
| **Invest EchoVoice** | Multi-language (Q1) | +15–20% activation from global studios |
| **Build shared SDK** | One-click install→deploy (Q1) | +15–20% platform activation |
| **Refresh discovery** | Filters, "new," recommendations (Q2) | +10–15% reach for new tools |
| **Reframe success** | 30d active studios, not installs | Align incentives to value |

**The ask:** Make the sunset call, fund Q1 work (R01 + R02), reframe the goal to leadership, respond to Twin Hearth with the lore-library proposal. Everything else flows from there.

