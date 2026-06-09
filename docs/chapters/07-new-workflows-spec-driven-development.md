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

In traditional teams, specs are often treated as temporary planning documents. In AI-native teams, the spec becomes a durable control artifact that aligns humans and machines on expected outcomes.

## Key points for your team

Spec-driven development shifts friction to the cheapest point in the lifecycle: before implementation. A 10-minute disagreement on intent can avoid days of rework across code, tests, security review, and release planning.

Effective specs are short and explicit. A practical structure:

- Why now: the business or user need.
- What changes: concrete scope.
- Success criteria: observable outcomes.
- Out of scope: what this change will not do.
- Constraints: policy, architecture, and compliance boundaries.

For agent workflows, this structure drastically improves output quality because it replaces open-ended prompting with constrained execution intent.

## What to review with your team

Review your last five non-trivial changes and ask:

- Which had explicit success criteria before coding?
- Which had clear out-of-scope boundaries?
- Which needed major rework due to misunderstood intent?

The answers will show where spec discipline creates immediate leverage.

Spec Kit and similar workflows are useful accelerators, but the core principle is tool-agnostic: code quality improves when intent quality improves.

## Put this into practice

Require a short spec for every change above a threshold of impact or complexity. Keep the template minimal and enforce completion in pull request metadata.

Check out the [GitHub Spec-Kit](https://github.com/github/spec-kit) for an open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.

Spec Kit can be tailored to your needs through two complementary systems - extensions and presets - plus project-local overrides for one-off adjustments.



<div class="chapter-nav">
    <a class="chapter-nav__button chapter-nav__button--secondary" href="../06-cloud-native-gave-us-the-substrate/">Previous chapter</a>
    <a class="chapter-nav__button chapter-nav__button--primary" href="../08-new-workflows-context-engineering/">Next chapter</a>
</div>
