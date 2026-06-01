---
name: paper2pdf
description: Format academic manuscripts into polished DOCX/PDF-style layouts using journal templates, publisher guidelines, sample PDFs, or SciSpace format links. Use when the user asks for 学术论文排版, PDF排版, 论文PDF格式, journal template formatting, manuscript layout, submission-ready PDF/DOCX, Wiley/JGR formatting, AGU formatting, SciSpace templates, or converting a manuscript into a journal-style PDF.
---

# Academic PDF Layout

Use this skill to turn an academic manuscript into a polished journal-style DOCX/PDF layout while preserving the manuscript's scientific content.

## Coordinate With Other Skills

- If creating, editing, rendering, or visually checking DOCX/PDF files, use the Documents skill/plugin workflow.
- If the source manuscript is a spreadsheet-heavy supplement, use the Spreadsheets skill for tables before placing them in the manuscript.
- Use the user's required Python environment when running local programs. In this workspace, the user has specified WSL `env_py3.11`.

## Intake

Collect or infer:

- target journal, publisher, template link, sample PDF, or journal author guideline
- source manuscript file (`.docx`, `.tex`, `.pdf`, Markdown, or plain text)
- required output format: DOCX, PDF, LaTeX, or both DOCX and PDF
- title, authors, affiliations, abstract, keywords, main text, acknowledgments, data/code availability, conflicts, references, figures, captions, and tables
- citation style and reference source, if supplied
- whether the task is only visual formatting or also includes language polishing

If exact journal rules are missing, proceed with a clean academic layout and mark journal-specific requirements that need confirmation.

## Workflow

1. Inspect the manuscript structure and identify missing sections or malformed elements.
2. Inspect the supplied template/guideline/sample. If the user supplies the SciSpace Wiley JGR link, read `references/scispace-wiley-jgr.md`.
3. Build a layout plan covering page size, margins, font, title block, headings, abstract, body, figures, tables, captions, references, appendices, and line/page numbering.
4. Preserve the scientific meaning, results, and conclusions unless the user explicitly asks for rewriting.
5. Apply formatting to a new DOCX or LaTeX source while keeping the original file unchanged.
6. Export or render to PDF when requested.
7. Visually inspect the output pages: title page, first body page, representative figure/table pages, references, and any dense equations or captions.
8. Fix layout defects such as clipped text, orphan headings, broken captions, unreadable tables, overlapping elements, inconsistent headings, and missing cross-references.
9. Deliver the formatted output and a short note listing any requirements that still need journal-side confirmation.

## Layout Rules

- Prefer official publisher/journal guidelines over third-party template pages when both are available.
- Treat third-party format pages as helpful references, not final authority for submission compliance.
- Keep a sober academic style: no decorative elements, no marketing layout, no ornamental colors.
- Preserve figure/table numbering, citations, equations, units, and scientific terminology.
- Do not fabricate references, author information, funding statements, ethics statements, line numbers, figure files, or supplementary material.
- If line numbers are required, add them only when the output tool supports stable line numbering.
- If the output is a journal-style PDF preview rather than a submission-ready file, state that clearly.

## Output Modes

- **Layout audit:** identify formatting problems and list exact fixes.
- **DOCX formatting:** produce a polished Word manuscript that follows the selected journal/template style as closely as possible.
- **PDF formatting:** produce or render a PDF-style manuscript and inspect visual quality.
- **Template conversion:** convert manuscript structure toward a supplied journal template while preserving content.
- **Source package:** provide DOCX/PDF plus any generated assets, logs, or notes needed for submission review.

## References

- Read `references/scispace-wiley-jgr.md` when the user provides the SciSpace Wiley Journal of Geophysical Research format link or requests Wiley/JGR-style manuscript layout.
