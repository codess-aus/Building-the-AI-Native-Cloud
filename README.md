# Building-the-AI-Native-Cloud

Conference companion site for the Building the AI-Native Cloud talk.

## Content source of truth

The website content is authored directly in:

- `docs/index.md`
- `docs/chapters/*.md`

Do not regenerate chapter content from `context.md`.

## Local workflow

1. Edit chapter files under `docs/chapters/`.
2. Build locally:

```bash
mkdocs build --strict
```

3. Preview locally if needed:

```bash
mkdocs serve
```

## Deployment

GitHub Actions deploys the existing authored markdown with MkDocs.
It does not run chapter generation.
