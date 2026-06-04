# Mid-Level Product Manager (AI) — Technical Assessment

**Time limit:** ~2 hours.

---

## Context

**Mythril** is a game-publishing company building **The Armory** — a self-serve, in-platform
storefront where game studios discover, install, and deploy AI-powered development tools
(art, audio, code, QA, narrative, design). Studios like **Twin Hearth Studios** (makers of the
dark-fantasy tactical RPG *Hollow Crown*) live in The Armory every day.

The storefront has been live for ~10 months and has grown to **12 tools across ~120 studios**.
Leadership is happy with the install numbers and wants to "double down on what's working,"
add more tools, and keep every customer happy. Your job is to tell them what *is* actually
working — and what isn't — and turn that into a plan.

You've just inherited the storefront as its PM. You have the raw operating data in `/data/`:

| File | What's in it |
|---|---|
| `tools.csv` | The 12 live/beta tools with current-state metrics: installs, 30-day active studios, week-4 retention, deploys per active studio, support tickets, CSAT, monthly infra cost. |
| `usage-monthly.csv` | 6 months of trajectory per tool: cumulative installs and 30-day active studios, month by month. |
| `intake-backlog.csv` | 9 open requests — new tools, tool investments, and platform capabilities — each with reach / impact / confidence / effort and a source note. |
| `studio-feedback.csv` | Verbatim quotes and support themes from studios about specific tools and the storefront itself. |

The data is realistic, not clean: headline numbers and ground truth don't always agree, the
loudest request isn't the most valuable one, and some tools are quietly costing more than
they return.

---

## The task

Produce **one decision-ready strategy document** (Markdown or PDF) that a Head of Product
could read in 15 minutes and act on. It must deliver all six:

1. **Storefront diagnosis & success metrics.** What's actually working vs. what only *looks*
   like it's working? Separate **reach** (installs) from **value** (activation, retention,
   engagement, satisfaction, cost). Name the real winners and the headline tool that's misleading
   leadership, backed by numbers. Then state the **north-star metric** you'd run the storefront on
   (and why "total installs" is the wrong one) plus the supporting leading/lagging metrics.

2. **An adoption plan.** Pick the 1–2 tools where you'd grow adoption first and say how — what's
   blocking studios from going from *install* to *recurring use*, and the concrete moves
   (discovery, onboarding, packaging) you'd make to increase it.

3. **Readiness calls: launch / invest / sunset.** Give the simple criteria you'd use to decide
   whether a tool is ready to **launch/graduate**, deserves **more investment**, or should be
   **sunset** — then apply them: which tool graduates from beta, which to double down on, and
   which to **cut** (quantify the rough infra + support savings of cutting them). Make the
   unglamorous call.

4. **A prioritized roadmap for the next 2 quarters.** Engineering capacity is limited and the
   backlog mixes new tools, tool investments, and platform capabilities. Use an explicit
   prioritization framework (e.g. RICE — show your math) to rank it. Justify your top bets, what
   you're **deprioritizing**, and how you'd sequence the work. Address the **technical/platform**
   items (APIs, the shared deploy/auth SDK) on their merits, not just the flashy tools.

5. **Stakeholder alignment.** Leadership's stated goal is "double down on installs" — which the
   data complicates. Write the short message (a few lines) you'd send to **(a) leadership** to
   re-frame the goal with evidence, and **(b) the Twin Hearth Studios sponsor** behind the loudest
   request, explaining where their ask lands on the roadmap and why. Handle it like a PM, not an
   order-taker.

6. **An intake-to-launch process.** A reusable lifecycle — intake → prioritization → build →
   launch → measurement → iteration (and a sunset gate) — so the next tool, and the one after
   that, is handled the same way every time. Keep it tight and usable, not a wall of text.

You don't need to be "correct" to a single decimal. We're grading your **methodology, judgment,
and the story you tell with the data** — a defensible, well-reasoned plan beats a confident
wrong one.

---

## Use AI to do the work

This is an **AI-first** role. Use whatever AI tools you like — to parse and cross-reference the
CSVs, compute RICE, find the signal hidden under the headline numbers, pressure-test your
prioritization, and draft the document. We care about the result and your judgment, not that
you typed it by hand.

You **must** include a short **`PM_AI_WORKFLOW.md`** (½–1 page) describing:
- which AI tool(s) you used and for what (analysis vs. drafting vs. sanity-checking),
- one prompt or workflow you're proud of,
- one place where the AI was wrong or misleading and how you caught it.

---

## Tooling

Use anything: a spreadsheet, a notebook, a few lines of Python/SQL, or just an AI assistant
reading the CSVs. If you write a script to crunch the data, commit it alongside your document.

## Out of scope

- No code, app, or UI to build. This is a product-thinking exercise.
- No need for pixel-perfect design or a slide deck — a clear written doc is the deliverable.
- Don't invent data you weren't given; if you assume something, state the assumption.

---

## What we're looking for

| Area | Weight |
|---|---|
| **Analytical accuracy & metrics** — found the real winners vs. the vanity headline, the right cuts, and the right north-star, grounded in the data | 25% |
| **Prioritization & roadmap** — explicit framework, defensible top bets (incl. the technical/platform items), sane sequencing | 20% |
| **Readiness & adoption** — sensible launch/invest/sunset criteria + a credible plan to grow adoption | 15% |
| **Stakeholder alignment & communication** — re-frames the flawed goal with evidence; handles the executive request like a PM, not an order-taker | 10% |
| **Intake-to-launch process** — clear, complete, genuinely reusable | 10% |
| **Effective use of AI** to do the work (and the `PM_AI_WORKFLOW.md`) | 10% |
| **Clarity** — is it decision-ready and skimmable? | 10% |

We are **not** grading polish or volume. A tight 3–4 page memo with the right calls beats a
20-page document that misses the story in the data.

---

## How to submit

1. **Fork** this repo.
2. Create branch `submission/<your-name>`.
3. Commit your strategy document, your `PM_AI_WORKFLOW.md`, and any analysis script/spreadsheet
   to an `/output/` folder.
4. Open a **Pull Request** to `main`.
5. In the PR description, include: **time spent** and a one-line summary of your top recommendation.
