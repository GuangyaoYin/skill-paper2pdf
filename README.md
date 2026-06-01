# Paper2PDF Skill

`paper2pdf` is a Codex skill for formatting academic manuscripts into polished journal-style DOCX and PDF layouts using journal templates, publisher guidelines, sample PDFs, or SciSpace format links.

## What It Does

- Audits manuscript structure and missing layout elements.
- Builds a layout plan for title blocks, headings, abstract, figures, tables, captions, references, appendices, and line/page numbering.
- Formats manuscripts into DOCX/PDF-style academic layouts while preserving scientific meaning.
- Uses supplied journal templates or guidelines when available.
- Includes a Wiley/Journal of Geophysical Research SciSpace reference for JGR-style layout tasks.
- Performs visual QA on rendered pages when document rendering is available.

## Installation

Install this skill into Codex from this repository:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo GuangyaoYin/skill-paper2pdf \
  --path paper2pdf
```

After installation, restart Codex so the new skill is loaded.

## Usage

```text
Use $paper2pdf to format my manuscript into a polished journal-style PDF using this template link: ...
```

Chinese example:

```text
使用 paper2pdf，把我的论文按照这个期刊模板排版并输出 PDF。
```

## Files

- `paper2pdf/SKILL.md`: main workflow and triggering instructions.
- `paper2pdf/references/scispace-wiley-jgr.md`: SciSpace Wiley/JGR format reference.
- `paper2pdf/agents/openai.yaml`: Codex UI metadata.

## Notes

This skill treats third-party template pages as helpful references, not final submission authorities. For formal submission, verify exact requirements against the current publisher or journal guidelines.
