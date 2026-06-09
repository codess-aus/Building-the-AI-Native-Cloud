---
title: "08 · New Workflows: Context Engineering"
description: "Why context quality drives output quality, and how to engineer context deliberately."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/7-context.png" alt="Hero illustration for chapter 08, New Workflows: Context Engineering">

<div class="sn-cat">Workflow</div>

</div>

# New Workflows: Context Engineering

*Why context quality drives output quality, and how to engineer context deliberately.*

## Why this chapter matters

Model capability is now broad enough that context quality has become the dominant performance variable in many engineering tasks.

When outputs are syntactically correct but strategically wrong, the issue is usually context starvation, not model failure.

## Key points for your team

Treat context as an engineered input with layers:

- Repository context: architecture, conventions, coding standards, decision records.
- Tool context: what systems the agent can query or modify.
- Task context: explicit objective, constraints, and acceptance criteria.

High-performing teams stop assuming context is "somewhere in the repo." They package the minimum context needed for the current task.

This is especially important for complex, cross-cutting changes where local file patterns are poor predictors of the right system-level decision.

## What to review with your team

Audit context readiness in one repository:

- Is there clear contributor guidance for humans and agents?
- Are architectural constraints documented where changes are made?
- Are tool permissions explicit and scoped?
- Do complex tasks include prepared context packets?

Most teams discover they have partial context assets but no repeatable packaging process.

Building that process yields outsized gains in quality and review speed.

## Put this into practice

For your next complex change, create a context packet with architecture notes, constraints, known risks, and success criteria. Compare the output quality and rework rate against your baseline.

<div class="chapter-nav">
    <a class="chapter-nav__button chapter-nav__button--secondary" href="../07-new-workflows-spec-driven-development/">Previous chapter</a>
    <a class="chapter-nav__button chapter-nav__button--primary" href="../09-new-operating-model-humans-agents/">Next chapter</a>
</div>
