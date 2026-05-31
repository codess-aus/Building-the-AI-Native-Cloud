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

Agents should be treated as a distinct identity class with constrained permissions and auditable behavior. Security outcomes depend on least privilege by design.

## Key points for your team

Security posture must evolve with the actor model. Agents are execution identities that need explicit boundaries, not implicit trust inherited from developer workflows.

The conference companion takeaway is to make policy concrete early: branch scope, secret access, and tool permissions should be explicit, reviewable, and enforced before broad rollout.

## Put this into practice

Define scope boundaries for branch access, secrets, and tool calls before rollout, and enforce them with policy controls.

<div class="chapter-nav" markdown>

<a class="chapter-nav__button chapter-nav__button--secondary" href="../10-reliability-at-scale/">Previous chapter</a>
<a class="chapter-nav__button chapter-nav__button--primary" href="../12-governance-at-scale/">Next chapter</a>

</div>
