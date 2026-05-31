---
title: "07 · New Workflows: Spec-Driven Development"
description: "How short, explicit specs improve alignment before implementation starts."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/6-sdd.png" alt="Hero illustration for chapter 07, New Workflows: Spec-Driven Development">

<div class="sn-cat">Workflow</div>

</div>

# New Workflows: Spec-Driven Development

*How short, explicit specs improve alignment before implementation starts.*

## Why this chapter matters

Spec-driven development reduces rework and ambiguity. It gives humans and agents a shared contract before implementation starts.

Spec-Driven Development flips the script on traditional software development. For decades, code has been king - specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: specifications become executable, directly generating working implementations rather than just guiding them.

Spec-Driven Development is a structured process that emphasizes:

- Intent-driven development where specifications define the "what" before the "how"
- Rich specification creation using guardrails and organizational principles
- Multi-step refinement rather than one-shot code generation from prompts
- Heavy reliance on advanced AI model capabilities for specification interpretation

## Key points for your team

Spec-driven work shifts debate to the right moment: before code is written. This reduces ambiguous implementation paths and helps both humans and AI systems align on expected outcomes.

As a conference companion takeaway, think of the spec as the minimum shared contract for change. Even brief specs can dramatically improve review quality, handoffs, and post-release accountability.

## What to review with your team

For team discussion, use this chapter to connect Spec is the **durable artifact**, 5 lines beats 50 pages, Sections: Why / What changes / Success criteria / Out of scope, and Cheaper to argue about a spec than a diff with your current delivery loop.

In the session context, The most uncomfortable change for engineers is this: the spec is now the durable artifact, and the code is downstream of it. Spec Kit formalizes this with a Specify, Plan, Tasks, Implement flow. Use that framing to align engineering, platform, and governance stakeholders on concrete next steps.

## Put this into practice

Use a short spec template with goal, user impact, success criteria, and out-of-scope for every non-trivial change.

Check out the [GitHub Spec-Kit](https://github.com/github/spec-kit) for an open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.

Spec Kit can be tailored to your needs through two complementary systems - extensions and presets - plus project-local overrides for one-off adjustments.



<div class="chapter-nav">
    <a class="chapter-nav__button chapter-nav__button--secondary" href="../06-cloud-native-gave-us-the-substrate/">Previous chapter</a>
    <a class="chapter-nav__button chapter-nav__button--primary" href="../08-new-workflows-context-engineering/">Next chapter</a>
</div>
