# Building the AI-Native Cloud
### A 20-Minute Talk for the Asia DevOps Conference

Master Chief Sparkle, here is a complete slide-by-slide design. I have built it for a 20-minute slot, which gives you roughly **12 content slides** at ~90 seconds each, plus an opener, a transition, and a close. I have weighted it toward your chapter's core thesis (AI-native is a *loop redesign*, not a tool bolt-on) and pulled the Asia DevOps audience toward the operational realities: reliability, security, governance.

For each slide you get:
- **The Thought** — the single idea the slide must land
- **Speaker Notes** — what you actually say (timed for pace)
- **Bullet Reminders** — what goes on the slide itself (sparse, deliberately)

---

## Slide 1 — Title (0:00 to 0:30)

**The Thought:** Set the frame: this is not a Copilot demo, this is an architecture conversation.

**Speaker Notes:**
> "Good morning. I'm here to talk about building the AI-native cloud. Not AI *in* the cloud, not AI *on top of* the cloud, but a cloud where AI agents are first-class participants in how we build, ship, and run software. In the next 20 minutes I want to convince you that the shift from cloud-native to AI-native is the same magnitude of change as the shift from on-prem to cloud, and most of us are still bolting AI onto an operating model that was never designed for it."

**Bullet Reminders:**
- Building the AI-Native Cloud
- From cloud-native to AI-native
- [Your name, role, handle]

---

## Slide 2 — The Quiet Shift (0:30 to 2:00)

**The Thought:** Something already changed. Most teams haven't noticed.

**Speaker Notes:**
> "Between the day Copilot suggested its first line of code and the day it started opening its own pull requests, something quietly shifted. It didn't arrive as one launch. It arrived as a stack: agent mode in the editor, coding agents on GitHub, the Model Context Protocol standardizing how tools plug into models, Spec Kit making the specification a durable artifact, AGENTS.md becoming the file where we tell AI teammates how to behave. The 2025 DORA report tells us roughly 90 percent of technologists now use AI at work. So the question is no longer *are you using AI*. The question is: *is your delivery loop designed for AI, or are you still bolting AI onto a loop designed without it?*"

**Bullet Reminders:**
- 2024 to 2026: a stack of compatible primitives
- Agent mode, coding agents, MCP, Spec Kit, AGENTS.md
- ~90% of technologists use AI at work (DORA 2025)
- New question: is your *loop* designed for AI?

---

## Slide 3 — Three Eras, Side by Side (2:00 to 3:30)

**The Thought:** Give the audience a vocabulary so they can locate themselves on the map.

**Speaker Notes:**
> "Three eras. Traditional: humans do every stage, AI is absent. AI-assisted: humans still drive, but Copilot helps at each step. The loop is unchanged, it just runs faster. AI-native: the loop itself is redesigned. Specs become first-class, context is engineered, agents run end-to-end stages, traces are auditable artifacts. The diagnostic question, next time someone says they're doing AI-native, is *which row of this table did their loop actually change?* If the answer is just *we turned on Copilot*, that's AI-assisted. Good place to be. Not the same thing."

**Bullet Reminders:**
| | Traditional | AI-Assisted | AI-Native |
|---|---|---|---|
| Unit of work | Ticket → code | Ticket → code (faster) | Spec → context → change → trace |
| Who edits | Human | Human + suggestions | Human and/or agent |
| Artifacts | Code, PR | Code, PR | Spec, context, trace, code, PR |
| Governance | Review, CI | Review, CI | + spec review, agent permissions, eval gates |

---

## Slide 4 — Defining AI-Native (3:30 to 4:30)

**The Thought:** A definition you can hold a team accountable to.

**Speaker Notes:**
> "Here is the definition I want you to leave with. AI-native software development means designing your delivery loop so AI isn't just helping developers, it's *participating* alongside them. Agents aren't tools you use. They're contributors you *design for*, with defined roles, guardrails, feedback loops, and accountability. Three words do the real work. *Designing*: it's a choice about the loop, not a checkbox on a tool. *Participating*: AI takes turns, opens PRs, files issues. *Accountable*: every agent action leaves a trail."

**Bullet Reminders:**
- AI is a **participant**, not a tool
- Designed for, not bolted on
- Every action leaves a trail
- Three words: **designing**, **participating**, **accountable**

---

## Slide 5 — The Six-Stage Loop (4:30 to 6:30)

**The Thought:** Show the anatomy. This is the spine of the rest of the talk.

**Speaker Notes:**
> "Six stages. Intent: captured deliberately, not in a Slack thread. Spec: an artifact in the repo, brief and reviewable in five minutes. Context: engineered through AGENTS.md, MCP servers, and per-task context packets. Change: made by a human, by agent mode, or by the coding agent, anchored on the spec. Verification: layered from cheap to expensive: tests, evaluators, policy gates, human review. Delivery: ships through your existing CI/CD and feeds production signals *back into the spec*, not just the backlog. The new artifact at the start is the spec. The new arrow at the end is the feedback into the spec. Everything else is rebalanced, not reinvented."

**Bullet Reminders:**
```
INTENT → SPEC → CONTEXT → CHANGE → VERIFICATION → DELIVERY
   ↑___________________________________________________|
          production signals feed back into the spec
```
- New artifact: **spec**
- New arrow: **feedback to spec**

---

## Slide 6 — Cloud-Native Gave Us the Substrate (6:30 to 7:30)

**The Thought:** Honour the audience's existing investments. AI-native rides on top of cloud-native, it doesn't replace it.

**Speaker Notes:**
> "I want to be clear with this audience: AI-native does not throw away cloud-native. It depends on it. Containers, declarative infrastructure, GitOps, observability, zero-trust networking, ephemeral environments: every one of these is a *prerequisite* for safe agent participation. The coding agent runs in an ephemeral environment because we learned to build ephemeral environments. It can be scoped to a branch because we learned branch protection. It can call an internal API through an MCP server because we learned service meshes and tokens. Cloud-native gave us the substrate. AI-native is what we build on it."

**Bullet Reminders:**
- Cloud-native = the substrate
- Ephemeral envs, GitOps, observability, zero-trust
- AI-native **depends on** cloud-native maturity
- No shortcut: weak substrate, weak agents

---

## Slide 7 — New Workflows: Spec-Driven Development (7:30 to 9:00)

**The Thought:** The spec is the durable artifact. Code is downstream.

**Speaker Notes:**
> "The most uncomfortable change for engineers is this: the spec is now the durable artifact, and the code is downstream of it. Spec Kit formalizes this with a Specify, Plan, Tasks, Implement flow. But you don't need the toolkit to start. A five-line Markdown file in a `specs/` folder with *why*, *what changes for the user*, *success criteria*, and *out of scope* is enough. The point is not to anticipate every edge case. The point is to give the agent and the reviewer a shared contract. And here's the quiet superpower: surfacing ambiguity in a spec review, before any code is written, is dramatically cheaper than catching it in a PR."

**Bullet Reminders:**
- Spec is the **durable artifact**
- 5 lines beats 50 pages
- Sections: Why / What changes / Success criteria / Out of scope
- Cheaper to argue about a spec than a diff

---

## Slide 8 — New Workflows: Context Engineering (9:00 to 10:30)

**The Thought:** Context is the second-most-important investment after the spec.

**Speaker Notes:**
> "Context is engineered, not assumed. Three layers. First, AGENTS.md: a plain Markdown file in the repo that tells agents how this codebase prefers to be edited. What library to use for dates. Which branches it can push to. Which conventions are non-negotiable. Second, MCP servers: the Model Context Protocol lets you expose your wiki, your observability platform, your internal APIs as first-class tools the agent can call. Writing a custom MCP server is a weekend project, not a quarter-long migration. Third, per-task context packets for non-trivial work. When an agent produces code that is locally plausible and globally wrong, the cause is almost always context starvation. Fix context, fix the agent."

**Bullet Reminders:**
- **AGENTS.md** — how this repo prefers to be edited
- **MCP servers** — wiki, observability, internal APIs as tools
- **Per-task context packets** for non-trivial work
- Bad output is usually **context starvation**

---

## Slide 9 — New Operating Model: Humans + Agents (10:30 to 12:00)

**The Thought:** Roles change. Headcount doesn't have to shrink. Ambition should expand.

**Speaker Notes:**
> "A colleague told me recently, *these are dark times to be developers. Small companies will cut three engineers and keep the two who can talk to the business and code faster with AI.* I disagree, strongly. Companies that think AI is about doing yesterday's work with fewer developers won't be around in two years. That's not transformation, that's decline. If you want to win with AI, you expand ambition, not shrink headcount. You give developers space to orchestrate fleets of agents, to apply judgment and creativity at a completely different scale. The operating model shift is this: engineers become **specifiers, context curators, and reviewers of intent.** The keyboard time goes down. The judgment time goes up. That is a more senior job, not a smaller one."

**Bullet Reminders:**
- Wrong race: cut headcount
- Right race: **expand ambition**
- New roles: **specifier, context curator, reviewer of intent**
- Less typing, more judgment

---

## Slide 10 — Reliability at Scale (12:00 to 13:30)

**The Thought:** Reliability isn't threatened by agents. It's threatened by *invisible* agents.

**Speaker Notes:**
> "Reliability in an AI-native cloud rests on one principle: **no invisible work**. Every agent run leaves a trace. Model version. Tools called. Files touched. Spec citation per commit. When something breaks at 2am, the on-call engineer has to be able to reconstruct *why* a change was made, not just *what* changed. Verification is layered, cheap to expensive: deterministic tests first, then AI evaluators checking the diff against the spec's success criteria, then policy gates including Advanced Security and Copilot Autofix, then human review focused on intent and integration. The funnel design is what makes the expensive layers economic. Treat agent PRs like any other contributor: sample one in ten for deep review, chosen at random. The moment you start skimming because they *look right*, you have drifted."

**Bullet Reminders:**
- No invisible work: **trace every run**
- Layered verification: tests → evaluators → policy → human
- Sample 1 in 10 agent PRs for deep review
- Trust calibration is a discipline, not a feeling

---

## Slide 11 — Security at Scale (13:30 to 15:00)

**The Thought:** Agents are a new identity class. Treat them like one.

**Speaker Notes:**
> "Security teams: an agent is a new identity class. It needs an identity, a scoped permission set, an audit trail, and a blast radius. Decide in week one, not after the near-miss. Which branches can an agent push to? Which MCP tools can it call? Which secrets must it *never* see? Write the answers in AGENTS.md and enforce them in branch protection and environment policies. Prompt injection is the new SQL injection: any text the agent reads, including issue comments, web pages fetched by tools, even file contents, is potentially adversarial. The mitigations are familiar in shape: least privilege, output validation, human approval gates for high-impact actions, and the principle that an agent should never hold a secret it cannot rotate."

**Bullet Reminders:**
- Agents are a **new identity class**
- Scope: branches, MCP tools, secrets, environments
- **Prompt injection** = the new SQL injection
- Least privilege, validated outputs, human gates on impact

---

## Slide 12 — Governance at Scale (15:00 to 16:30)

**The Thought:** Governance designed on day one is cheap. Governance bolted on after an incident is expensive.

**Speaker Notes:**
> "Governance is where most teams will stumble in 2026. Three practical moves. One: make AGENTS.md a reviewed artifact, just like code. Changes to it go through PR review. Two: preserve agent run summaries on every PR, model version included. In regulated industries this is a compliance question, not a nice-to-have. Auditors will ask *which model made this change, with what tools, against which spec*. You want the answer to be a link, not an investigation. Three: set anti-goals explicitly. Write down what you are *not* trying to optimize for. *Maximum agent autonomy at the expense of accountability* is an anti-goal. *AI did it* is never a sufficient explanation in a post-incident review. Anti-goals are where hard-won wisdom lives."

**Bullet Reminders:**
- AGENTS.md is a **reviewed artifact**
- Preserve run traces: model, tools, files, spec
- Auditors will ask. Make the answer a link.
- Write **anti-goals**, not just goals

---

## Slide 13 — Seven Failure Modes (16:30 to 18:00)

**The Thought:** Pattern-match these now. Save yourself a quarter.

**Speaker Notes:**
> "Seven failure modes will hit you in the first six months. I'll name them fast and you'll recognize at least two. *Vibe-driven development*: plausible diff, hidden bug. Fix: no agent run without a spec. *Context starvation*: locally plausible, globally wrong. Fix: invest in AGENTS.md and MCP. *Trust drift*: you start skimming. Fix: random deep-review sampling. *Mistaking the agent for the loop*: productivity bump, declare victory, stop investing. Fix: the artifacts make the loop better, the agent is one participant. *Invisible agent work*: future incident waiting. Fix: preserve traces. *Deferring governance*: locking down after a near-miss costs more. Fix: decide permissions in week one. *Confusing productivity with capability*: faster typing is not a better loop. Fix: measure artifact quality, not throughput."

**Bullet Reminders:**
1. Vibe-driven development → write a spec
2. Context starvation → AGENTS.md + MCP
3. Trust drift → random deep reviews
4. Agent ≠ loop → invest in artifacts
5. Invisible work → preserve traces
6. Deferred governance → decide in week one
7. Productivity ≠ capability → measure artifacts

---

## Slide 14 — One-Page Memo (18:00 to 19:00)

**The Thought:** Give them something they can implement on Monday.

**Speaker Notes:**
> "Here is what I want you to take back. One page. The AI-Native Success Criteria Memo. Loop scope: when do *you* consider your loop AI-native? Artifact criteria: what does every change retain? Quality bars: what blocks a merge? Human responsibility: *which* human, named by role? Anti-goals: what are you deliberately not optimizing for? Review cadence: quarterly, with an owner. Write v1 this week. It should be slightly embarrassing in its specificity, not polished for a slide. A bar the team routinely ignores teaches everyone the memo is decorative. The memo is a target, not a description of done. But it's the artifact that turns this talk into practice."

**Bullet Reminders:**
- **AI-Native Success Criteria Memo v1**
- Loop scope · Artifacts · Quality bars
- Human responsibility · Anti-goals · Cadence
- Write it this week. Embarrass yourself slightly.

---

## Slide 15 — Close and Three Questions (19:00 to 20:00)

**The Thought:** Leave them with questions they cannot un-ask.

**Speaker Notes:**
> "Three questions to carry home. One: on your team's last non-trivial change, who actually decided what *done* meant? A human, an agent, or no one in particular? Two: which stage of your current loop would change least if every AI capability turned off tomorrow? That's where you're still doing traditional or AI-assisted work. Three: which of the seven failure modes is most likely to bite your team first? Write it on a sticky note before you leave this room. The AI-native cloud is not a product you buy. It's a loop you design. Thank you."

**Bullet Reminders:**
- Who decided *done*?
- Which stage survives AI turning off?
- Which failure mode bites first?
- **The AI-native cloud is a loop you design.**
- Thank you · [contact / repo link]

---

## Timing Summary

| Section | Slides | Duration |
|---|---|---|
| Open and frame | 1 to 4 | 4:30 |
| The loop and the substrate | 5 to 6 | 3:00 |
| New workflows | 7 to 8 | 3:00 |
| Operating model | 9 | 1:30 |
| Reliability, security, governance | 10 to 12 | 4:30 |
| Failure modes and the memo | 13 to 14 | 2:30 |
| Close | 15 | 1:00 |
| **Total** | **15** | **20:00** |

