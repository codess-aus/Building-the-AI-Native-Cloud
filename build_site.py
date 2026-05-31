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

SLIDE_HEADING = re.compile(r"^## Slide (\d+) — (.+?) \((.+?)\)$", re.MULTILINE)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


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
        title = match.group(2).strip()
        timing = match.group(3).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else text.index("\n## Timing Summary")
        body = text[start:end].strip()

        thought = extract_section(body, "**The Thought:**", "**Speaker Notes:**")
        notes = extract_section(body, "**Speaker Notes:**", "**Bullet Reminders:**")
        bullets = body.split("**Bullet Reminders:**", 1)[1].strip()
        bullets = re.sub(r"\n+---\s*$", "", bullets).strip()

        slides.append(
            {
                "number": f"{slide_number:02d}",
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
description: A responsive, accessible MkDocs site for the talk chapters.
---

<div class="home-hero">
  <div class="home-hero__panel">
    <p class="home-hero__eyebrow">Asia DevOps Conference Series</p>
    <h1>Building the AI-Native Cloud</h1>
    <p class="home-hero__lede">A responsive MkDocs site with one chapter for each slide, accessible light and dark modes, and the talk content laid out under every hero image.</p>
    <div class="home-hero__actions">
            <a class="button button--primary" href="chapters/{slides[0]['page_name']}/">Start with the opener</a>
      <a class="button button--secondary" href="#chapters">Browse chapters</a>
    </div>
  </div>
</div>

<section class="home-strip" aria-label="Site features">
  <div>
    <strong>Accessible</strong>
    <span>Semantic markup, strong contrast, visible focus states.</span>
  </div>
  <div>
    <strong>Responsive</strong>
    <span>Cards and hero images reflow cleanly from mobile to desktop.</span>
  </div>
  <div>
    <strong>Theme switch</strong>
    <span>Light mode stays white with black text. Dark mode stays black with white text.</span>
  </div>
</section>

## Chapters

<a id="chapters"></a>

<div class="chapter-grid">
{chr(10).join(cards)}
</div>
"""
    ).strip() + "\n"


def render_chapter(slide: dict[str, str], asset_name: str) -> str:
    return textwrap.dedent(
        f"""---
title: {slide['number']}. {slide['page_title']}
description: {slide['thought']}
---

[Back to home](../index.md)

<p class="chapter-meta">Slide {slide['number']} · {slide['timing']}</p>

<div class="chapter-hero">
![{slide['title']}](../assets/{asset_name})
</div>

## The Thought

{slide['thought']}

## Slide Copy

{slide['bullets']}

<details class="speaker-notes">
<summary>Speaker notes</summary>

{slide['notes']}

</details>
"""
    ).strip() + "\n"


def main() -> None:
    slides = parse_context()
    if len(slides) != len(SOURCE_IMAGES):
        raise RuntimeError(f"Expected {len(SOURCE_IMAGES)} slides, found {len(slides)}")

    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    (DOCS / "index.md").write_text(render_index(slides), encoding="utf-8")

    for slide in slides:
        asset_name = SOURCE_IMAGES[int(slide["number"]) - 1]
        chapter_path = CHAPTERS_DIR / f"{slide['page_name']}.md"
        chapter_path.write_text(render_chapter(slide, asset_name), encoding="utf-8")


if __name__ == "__main__":
    main()