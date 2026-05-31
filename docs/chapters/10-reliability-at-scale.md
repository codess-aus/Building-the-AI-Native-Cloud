---
title: 10. Reliability at Scale
description: Reliability isn't threatened by agents. It's threatened by *invisible* agents.
---

[Back to home](../index.md)

<p class="chapter-meta">Slide 10 · 12:00 to 13:30</p>

<div class="chapter-hero">
![Reliability at Scale](../assets/9-reliability.png)
</div>

## The Thought

Reliability isn't threatened by agents. It's threatened by *invisible* agents.

## Slide Copy

- No invisible work: **trace every run**
- Layered verification: tests → evaluators → policy → human
- Sample 1 in 10 agent PRs for deep review
- Trust calibration is a discipline, not a feeling

<details class="speaker-notes">
<summary>Speaker notes</summary>

> "Reliability in an AI-native cloud rests on one principle: **no invisible work**. Every agent run leaves a trace. Model version. Tools called. Files touched. Spec citation per commit. When something breaks at 2am, the on-call engineer has to be able to reconstruct *why* a change was made, not just *what* changed. Verification is layered, cheap to expensive: deterministic tests first, then AI evaluators checking the diff against the spec's success criteria, then policy gates including Advanced Security and Copilot Autofix, then human review focused on intent and integration. The funnel design is what makes the expensive layers economic. Treat agent PRs like any other contributor: sample one in ten for deep review, chosen at random. The moment you start skimming because they *look right*, you have drifted."

</details>
