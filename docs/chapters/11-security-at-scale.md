---
title: "11 · Security at Scale"
description: "Treating agents as execution identities with explicit boundaries and least-privilege controls."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/10-security.png" alt="Hero illustration for chapter 11, Security at Scale">

<div class="sn-cat">Security</div>

</div>

# Security at Scale

*Treating agents as execution identities with explicit boundaries and least-privilege controls.*

## Why this chapter matters

Security teams have a clear new requirement: treat agents as first-class execution identities.

If agents inherit broad human-level access without tight scoping, blast radius expands faster than controls can adapt.

## Key points for your team

A practical security model for agents includes:

- Identity: every agent action is attributable.
- Scope: permissions are bounded by task, environment, and tool.
- Isolation: execution happens in controlled boundaries.
- Validation: outputs are checked before high-impact actions.

Prompt injection and context poisoning are now routine threat vectors. Teams should model them explicitly, not treat them as edge cases.

Least privilege is no longer just an infrastructure concern. It is a workflow design concern.

## What to review with your team

Walk through one end-to-end scenario where an agent modifies production-impacting code:

- What identity does it run as?
- What can it read and write?
- Which secrets are reachable?
- What gates block unsafe release?

If you cannot answer these quickly, security design is under-specified.

Documented boundaries increase both safety and engineering velocity because teams spend less time debating ad hoc exceptions.

## Put this into practice

Create an agent permission matrix by repository and environment, then enforce it with policy and runtime controls before increasing autonomy.

<div class="chapter-nav">
    <a class="chapter-nav__button chapter-nav__button--secondary" href="../10-reliability-at-scale/">Previous chapter</a>
    <a class="chapter-nav__button chapter-nav__button--primary" href="../12-governance-at-scale/">Next chapter</a>
</div>
