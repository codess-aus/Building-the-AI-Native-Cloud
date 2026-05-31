from __future__ import annotations

import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
CHAPTERS_DIR = DOCS / "chapters"

SOURCE_IMAGES = [
    "0-title.png",
    "1-quiet.png",
    "2-3waves.png",
    "3-ainative.png",
    "4-loop.png",
    "5-substrate.png",
    "6-sdd.png",
    "7-context.png",
    "8-humansandagents.png",
    "9-reliability.png",
    "10-security.png",
    "11-governance.png",
    "12-failure.png",
    "13-memo.png",
    "14-questions.png",
]

EM_DASH = "\u2014"
SLIDE_HEADING = re.compile(r"^## Slide (\d+) " + EM_DASH + r" (.+?) \((.+?)\)$", re.MULTILINE)

CHAPTER_META = {
    1: {
        "category": "Opening",
        "subtitle": "Why this conversation matters now, and how to evaluate AI-native delivery through a trust-first lens.",
        "why": "This opening chapter sets the frame for the talk: AI-native delivery is not about adding one more tool, it is about changing how teams decide, build, verify, and ship.",
        "narrative": "The opening challenge is simple: if AI capability keeps accelerating, governance and delivery discipline must accelerate with it. This chapter invites you to evaluate your current practices through that lens, not through vendor claims or feature announcements.\n\nAs you revisit this with your team, use it as a framing conversation: what standards stay fixed regardless of tooling, and where does your current workflow still assume purely human execution?",
        "practice": "Use the trust question at the start of planning, architecture reviews, and go-live decisions so the same standard is applied throughout delivery.",
    },
    2: {
        "category": "Opening",
        "subtitle": "What has already changed in software delivery, and why intentional operating models now matter.",
        "why": "Most teams already use AI daily. The shift now is from ad-hoc usage to an intentional operating model where AI work is part of the delivery system.",
        "narrative": "The quiet shift is that AI is already embedded in day-to-day engineering work, whether or not organizations have formalized policy around it. What changed first was behavior; governance and process are now catching up.\n\nFor attendees, the practical takeaway is to stop treating AI usage as exceptional. Treat it as normal engineering work that needs the same clarity around ownership, verification, and accountability as any other production change.",
        "practice": "Map where AI is already present in your workflow, then identify one stage that still depends on informal process and make it explicit.",
    },
    3: {
        "category": "Foundation",
        "subtitle": "A practical model for understanding where your team is today and what AI-native progress really means.",
        "why": "Shared language reduces confusion. This chapter helps teams distinguish traditional, AI-assisted, and AI-native ways of working without overclaiming maturity.",
        "narrative": "This chapter is a positioning tool. It helps teams avoid speaking past each other by defining concrete differences between traditional, AI-assisted, and AI-native loops.\n\nUse it to make planning discussions more honest: if the loop has not changed, you are optimizing execution speed, not redesigning delivery. That distinction is useful, especially when prioritizing platform and governance investments.",
        "practice": "Choose the row in the maturity table that best describes your current loop and define one change needed to move to the next stage.",
    },
    4: {
        "category": "Foundation",
        "subtitle": "A shared definition your team can use to align delivery decisions, controls, and accountability.",
        "why": "A practical definition keeps teams aligned. AI-native delivery treats AI systems as accountable participants, not as hidden automation behind developer tools.",
        "narrative": "Definitions matter because they influence architecture, risk posture, and team expectations. Here, AI-native means AI participates in the workflow in ways that can be reviewed and governed, not merely assisted by autocomplete.\n\nFor conference attendees, this is a useful standard to carry home: if contribution cannot be traced and reviewed, it should not be treated as production-ready regardless of how fast it was produced.",
        "practice": "Add explicit ownership and auditability requirements to your team definition of done for any AI-assisted or agent-generated change.",
    },
    5: {
        "category": "Foundation",
        "subtitle": "How to break delivery into explicit stages so quality and risk are managed on purpose.",
        "why": "The six-stage loop shows where quality is created and where risk is introduced. Making each stage explicit improves handoffs and governance.",
        "narrative": "The six-stage model turns a vague delivery idea into a system that teams can inspect and improve. Instead of treating development as one continuous stream, it highlights where decisions are made and where controls should exist.\n\nAttendees can use this as a workshop artifact with engineering and platform teams: map each stage to current tooling and identify where missing artifacts or unclear ownership create avoidable risk.",
        "practice": "Document your loop from intent to delivery and add one concrete quality gate to each stage.",
    },
    6: {
        "category": "Foundation",
        "subtitle": "Why strong cloud-native foundations are the prerequisite for safe and scalable AI-native practices.",
        "why": "AI-native delivery depends on strong cloud-native engineering fundamentals. Teams with mature platform practices can adopt agents more safely and effectively.",
        "narrative": "This chapter reinforces that AI-native capability is built on top of cloud-native discipline. Containers, policy controls, observability, and secure environments are not optional extras; they are preconditions for safe autonomy.\n\nThe attendee takeaway is to avoid skipping maturity steps. If baseline platform reliability or security is weak, adding higher agent autonomy usually amplifies fragility rather than accelerating outcomes.",
        "practice": "Prioritize platform hygiene first: ephemeral environments, policy-based deployment, and observable services before broadening agent autonomy.",
    },
    7: {
        "category": "Workflow",
        "subtitle": "How short, explicit specs improve alignment before implementation starts.",
        "why": "Spec-driven development reduces rework and ambiguity. It gives humans and agents a shared contract before implementation starts.",
        "narrative": "Spec-driven work shifts debate to the right moment: before code is written. This reduces ambiguous implementation paths and helps both humans and AI systems align on expected outcomes.\n\nAs a conference companion takeaway, think of the spec as the minimum shared contract for change. Even brief specs can dramatically improve review quality, handoffs, and post-release accountability.",
        "practice": "Use a short spec template with goal, user impact, success criteria, and out-of-scope for every non-trivial change.",
    },
    8: {
        "category": "Workflow",
        "subtitle": "Why context quality drives output quality, and how to engineer context deliberately.",
        "why": "Context quality determines output quality. AI systems perform best when repository conventions, tool access, and task intent are made explicit.",
        "narrative": "When output is locally plausible but globally wrong, the root cause is often context quality rather than model quality. This chapter highlights context as an engineering asset that should be curated deliberately.\n\nAttendees can apply this immediately by improving repository guidance and tool boundaries so generated changes reflect architectural intent, operational constraints, and domain standards.",
        "practice": "Create or refine AGENTS.md and package context for complex tasks so generated changes reflect system-level intent, not just local code patterns.",
    },
    9: {
        "category": "Operating Model",
        "subtitle": "How teams can increase ambition and leverage by redesigning roles around intent and accountability.",
        "why": "The goal is not smaller ambition with fewer people. The opportunity is higher-leverage engineering where humans focus on decisions, constraints, and outcomes.",
        "narrative": "This chapter reframes the organizational question from replacement to leverage. High-performing teams use AI to increase scope and quality of what they can responsibly deliver, not just to cut implementation time.\n\nThe practical conference takeaway is role clarity: teams need people who can define intent, shape constraints, and review integrated outcomes, not only produce diffs quickly.",
        "practice": "Redefine role expectations to include specification, context curation, and review of intent, not only implementation throughput.",
    },
    10: {
        "category": "Reliability",
        "subtitle": "Building reliability through traceability, layered verification, and clear review boundaries.",
        "why": "Reliability requires traceability. Teams need to understand why a change happened, how it was validated, and what signals informed release decisions.",
        "narrative": "Reliability in AI-native systems depends on visibility. If teams cannot reconstruct why a generated change was made and how it passed verification, they cannot operate confidently at scale.\n\nFor attendees, this chapter is an operational reminder: reliability is a socio-technical property. Good traces, layered validation, and clear review boundaries are as important as test pass rates.",
        "practice": "Capture model version, tools used, files touched, and test evidence on every agent-generated pull request.",
    },
    11: {
        "category": "Security",
        "subtitle": "Treating agents as execution identities with explicit boundaries and least-privilege controls.",
        "why": "Agents should be treated as a distinct identity class with constrained permissions and auditable behavior. Security outcomes depend on least privilege by design.",
        "narrative": "Security posture must evolve with the actor model. Agents are execution identities that need explicit boundaries, not implicit trust inherited from developer workflows.\n\nThe conference companion takeaway is to make policy concrete early: branch scope, secret access, and tool permissions should be explicit, reviewable, and enforced before broad rollout.",
        "practice": "Define scope boundaries for branch access, secrets, and tool calls before rollout, and enforce them with policy controls.",
    },
    12: {
        "category": "Governance",
        "subtitle": "Designing governance early so speed and accountability can scale together.",
        "why": "Governance is most effective when introduced early. Waiting until incidents occur makes controls more costly and less trusted by delivery teams.",
        "narrative": "Governance works best when it is designed as part of delivery, not layered in after incidents. Early governance establishes expectations and reduces friction between engineering speed and risk management.\n\nAttendees can use this chapter to align legal, security, and platform perspectives around shared artifacts, auditability, and exception handling before scale introduces complexity.",
        "practice": "Review governance artifacts in the same cadence as code quality artifacts, including run traces and policy exceptions.",
    },
    13: {
        "category": "Failure Modes",
        "subtitle": "Recognizing common failure patterns early and turning them into concrete safeguards.",
        "why": "Known failure patterns help teams avoid repeating preventable mistakes. Naming these patterns builds shared vigilance across engineering, security, and operations.",
        "narrative": "The value of failure modes is not prediction accuracy, it is preparedness. Teams that can name likely failure patterns earlier can design practical safeguards before those risks materialize in production.\n\nFor conference attendees, this chapter is a facilitation tool: use it to run a lightweight risk workshop and convert each likely failure mode into one concrete mitigation owned by the team.",
        "practice": "Pick the two failure modes most likely for your team and define countermeasures before broadening AI usage.",
    },
    14: {
        "category": "Action Plan",
        "subtitle": "Turning conference insight into a living operating document your team can execute.",
        "why": "A one-page implementation memo turns ideas into execution. It creates a concrete baseline for accountability, measurement, and iteration.",
        "narrative": "This chapter translates strategy into a durable operating artifact. A short, explicit memo is easier to review, teach, and update than broad slide commitments.\n\nThe attendee takeaway is practical: publish a v1 quickly, use it in real decisions, and improve it through cadence. Maturity comes from iteration under real delivery pressure.",
        "practice": "Publish a version-one memo with explicit success criteria and anti-goals, then review and revise it on a fixed cadence.",
    },
    15: {
        "category": "Closing",
        "subtitle": "Reflection prompts to help your team carry trust and accountability into day-to-day delivery.",
        "why": "The closing chapter helps teams leave with practical reflection questions that translate conference insight into immediate action.",
        "narrative": "The closing section is designed to make the content portable. Good conference ideas become valuable only when they are reused in planning meetings, architecture reviews, and retrospectives.\n\nUse the reflection prompts as a repeatable discussion pattern to keep your team focused on trust, accountability, and long-term capability growth.",
        "practice": "Use the three closing questions in your next retrospective, architecture review, or release readiness discussion.",
    },
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def remove_emdash(value: str) -> str:
    return value.replace("\u2014", "-")


def extract_section(body: str, start_marker: str, end_marker: str | None) -> str:
    start = body.index(start_marker) + len(start_marker)
    if end_marker is None:
        return body[start:].strip()
    end = body.index(end_marker, start)
    return body[start:end].strip()


def parse_context() -> list[dict[str, str]]:
    text = (ROOT / "context.md").read_text(encoding="utf-8")
    matches = list(SLIDE_HEADING.finditer(text))
    slides: list[dict[str, str]] = []

    for index, match in enumerate(matches):
        slide_number = int(match.group(1))
        title = remove_emdash(match.group(2).strip())
        timing = match.group(3).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else text.index("\n## Timing Summary")
        body = text[start:end].strip()

        thought = remove_emdash(extract_section(body, "**The Thought:**", "**Speaker Notes:**"))
        notes = remove_emdash(extract_section(body, "**Speaker Notes:**", "**Bullet Reminders:**"))
        bullets = body.split("**Bullet Reminders:**", 1)[1].strip()
        bullets = re.sub(r"\n+---\s*$", "", bullets).strip()
        bullets = remove_emdash(bullets)
        filtered_lines = []
        for line in bullets.splitlines():
            lowered = line.lower()
            if "[your name" in lowered or "[contact / repo link]" in lowered:
                continue
            filtered_lines.append(line)
        bullets = "\n".join(filtered_lines).strip()

        slides.append(
            {
                "number": f"{slide_number:02d}",
                "number_int": slide_number,
                "title": title,
                "page_title": "Building the AI-Native Cloud" if slide_number == 1 else title,
                "timing": timing,
                "slug": slugify(title),
                "page_name": f"{slide_number:02d}-{slugify(title)}",
                "thought": thought,
                "notes": notes,
                "bullets": bullets,
            }
        )

    return slides


def yaml_quote(value: str) -> str:
    return value.replace('"', '\\"')


def clean_notes(notes: str) -> str:
    text = remove_emdash(notes.strip())
    text = re.sub(r"^>\s*\"?", "", text)
    text = text.rstrip('"').strip()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    replacements = {
        "Good morning. ": "",
        "I'm here to talk about": "This chapter explores",
        "I want to convince you that": "The key point is that",
        "I want you to leave with": "Attendees can leave with",
        "I want you to": "Attendees are encouraged to",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def first_sentences(text: str, count: int = 2) -> str:
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    if not sentences:
        return text
    return " ".join(sentences[:count]).strip()


def format_phrase_list(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def build_review_section(slide: dict[str, str]) -> str:
    bullets = []
    for line in slide["bullets"].splitlines():
        line = line.strip()
        if line.startswith("- "):
            bullets.append(line[2:].strip())

    cleaned_notes = clean_notes(slide["notes"])
    note_excerpt = first_sentences(cleaned_notes, count=2)

    if bullets:
        bullet_text = format_phrase_list(bullets)
        paragraph_one = (
            "For team discussion, use this chapter to connect "
            f"{bullet_text} with your current delivery loop."
        )
    else:
        paragraph_one = (
            "For team discussion, focus on how this chapter can be translated "
            "into explicit workflow decisions and accountability points."
        )

    paragraph_two = (
        f"In the session context, {note_excerpt} "
        "Use that framing to align engineering, platform, and governance stakeholders on concrete next steps."
    )

    return f"{paragraph_one}\n\n{paragraph_two}"


def chapter_meta(slide_number: int) -> dict[str, str]:
    meta = CHAPTER_META.get(
        slide_number,
        {
            "category": "Chapter",
            "subtitle": "A practical takeaway chapter for applying AI-native delivery in your own environment.",
            "why": "This chapter provides context and practical guidance for building AI-native delivery workflows.",
            "practice": "Identify one concrete improvement and test it in your next sprint.",
            "narrative": "Use this chapter as a discussion guide with your team to convert ideas into concrete workflow improvements.",
        },
    )
    return {key: remove_emdash(value) for key, value in meta.items()}


def render_index(slides: list[dict[str, str]]) -> str:
    card_template = textwrap.dedent(
        """
        <a class="chapter-card" href="chapters/{slug}/" aria-label="Open {number}. {title}">
          <img src="assets/{asset_name}" alt="Slide image for {title}">
          <div class="chapter-card__body">
            <p class="chapter-card__tag">Chapter {number}</p>
            <h2 class="chapter-card__title">{title}</h2>
            <p class="chapter-card__description">{thought}</p>
          </div>
        </a>
        """
    ).strip()

    cards = []
    for slide in slides:
        cards.append(
            card_template.format(
                slug=slide["page_name"],
                number=slide["number"],
                title=slide["page_title"],
                thought=slide["thought"],
                asset_name=SOURCE_IMAGES[int(slide["number"]) - 1],
            )
        )

    return textwrap.dedent(
        f"""---
title: Building the AI-Native Cloud
description: Chapter-by-chapter resources for conference attendees from the Building the AI-Native Cloud talk.
---

<div class="home-hero">
  <div class="home-hero__panel">
        <p class="home-hero__eyebrow">Conference Companion Guide</p>
    <h1>Building the AI-Native Cloud</h1>
        <p class="home-hero__lede">A chapter-by-chapter resource for conference attendees to revisit key ideas, share with teams, and turn insights into action after the session.</p>
    <div class="home-hero__actions">
            <a class="button button--primary" href="chapters/{slides[0]['page_name']}/">Start with chapter 01</a>
      <a class="button button--secondary" href="#chapters">Browse chapters</a>
    </div>
  </div>
</div>

## Chapters

<a id="chapters"></a>

<div class="chapter-grid">
{chr(10).join(cards)}
</div>
"""
    ).strip() + "\n"


def render_chapter(
    slide: dict[str, str],
    asset_name: str,
    prev_target: str,
    next_target: str,
    prev_label: str,
    next_label: str,
) -> str:
    meta = chapter_meta(slide["number_int"])
    review_section = build_review_section(slide)
    return textwrap.dedent(
        f"""---
title: "{slide['number']} · {yaml_quote(slide['page_title'])}"
description: "{yaml_quote(meta['subtitle'])}"
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/{asset_name}" alt="Hero illustration for chapter {slide['number']}, {slide['page_title']}">

<div class="sn-cat">{meta['category']}</div>

</div>

# {slide['page_title']}

*{meta['subtitle']}*

## Why this chapter matters

{meta['why']}

## Key points for your team

{meta['narrative']}

## What to review with your team

{review_section}

## Put this into practice

{meta['practice']}

<div class="chapter-nav">
    <a class="chapter-nav__button chapter-nav__button--secondary" href="{prev_target}">{prev_label}</a>
    <a class="chapter-nav__button chapter-nav__button--primary" href="{next_target}">{next_label}</a>
</div>
"""
    ).strip() + "\n"


def main() -> None:
    slides = parse_context()
    if len(slides) != len(SOURCE_IMAGES):
        raise RuntimeError(f"Expected {len(SOURCE_IMAGES)} slides, found {len(slides)}")

    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    (DOCS / "index.md").write_text(render_index(slides), encoding="utf-8")

    page_name_by_number = {slide["number_int"]: slide["page_name"] for slide in slides}

    for slide in slides:
        asset_name = SOURCE_IMAGES[int(slide["number"]) - 1]
        prev_target = "../../" if slide["number_int"] == 1 else f"../{page_name_by_number[slide['number_int'] - 1]}/"
        next_target = "../../" if slide["number_int"] == len(SOURCE_IMAGES) else f"../{page_name_by_number[slide['number_int'] + 1]}/"
        prev_label = "Back to home" if slide["number_int"] == 1 else "Previous chapter"
        next_label = "Back to home" if slide["number_int"] == len(SOURCE_IMAGES) else "Next chapter"
        chapter_path = CHAPTERS_DIR / f"{slide['page_name']}.md"
        chapter_path.write_text(
            render_chapter(slide, asset_name, prev_target, next_target, prev_label, next_label),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()