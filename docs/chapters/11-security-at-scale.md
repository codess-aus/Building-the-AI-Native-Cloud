---
title: 11. Security at Scale
description: Agents are a new identity class. Treat them like one.
---

[Back to home](../index.md)

<p class="chapter-meta">Slide 11 · 13:30 to 15:00</p>

<div class="chapter-hero">
![Security at Scale](../assets/10-security.png)
</div>

## The Thought

Agents are a new identity class. Treat them like one.

## Slide Copy

- Agents are a **new identity class**
- Scope: branches, MCP tools, secrets, environments
- **Prompt injection** = the new SQL injection
- Least privilege, validated outputs, human gates on impact

<details class="speaker-notes">
<summary>Speaker notes</summary>

> "Security teams: an agent is a new identity class. It needs an identity, a scoped permission set, an audit trail, and a blast radius. Decide in week one, not after the near-miss. Which branches can an agent push to? Which MCP tools can it call? Which secrets must it *never* see? Write the answers in AGENTS.md and enforce them in branch protection and environment policies. Prompt injection is the new SQL injection: any text the agent reads, including issue comments, web pages fetched by tools, even file contents, is potentially adversarial. The mitigations are familiar in shape: least privilege, output validation, human approval gates for high-impact actions, and the principle that an agent should never hold a secret it cannot rotate."

</details>
