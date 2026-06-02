# LaTeX PDF Workflow For Standard Equations

Use this reference when a PDF must contain standard mathematical equation typesetting comparable to Word Equation Editor or academic LaTeX PDFs. Do not use equation screenshots, formula PNGs, remote equation image URLs, or ASCII-only formulas unless the user explicitly asks for a fallback.

## When To Use

- The user asks for standard, native, or Word-equation-editor-like formulas in PDF.
- The document has dense derivations, matrices, aligned equations, vector/tensor notation, integrals, sums, or Greek symbols.
- A Markdown/ReportLab conversion has produced raw LaTeX, oversized formula images, missing glyphs, or square-box symbols.
- The deliverable should include editable source plus a PDF.

## Toolchain Check

Before writing final output, check for LaTeX engines:

```powershell
Get-Command xelatex,pdflatex,lualatex,tectonic,pandoc -ErrorAction SilentlyContinue
```

Preferred engines:

1. `xelatex`: best default for Chinese/CJK technical reports and Unicode text.
2. `lualatex`: good Unicode alternative when templates support it.
3. `pdflatex`: acceptable for Latin-only manuscripts or templates that require it.
4. `tectonic`: acceptable fallback for many simple LaTeX documents.

If none is installed, read `toolchain-install.md` and install only the missing component needed for the current route. Do not fake math with images or ASCII unless the user explicitly asks for that fallback.

The bundled helper `scripts/compile_latex_pdf.py` performs this check and runs the compile passes. Prefer it when available. On Windows, `scripts/install_latex_toolchain.ps1` can install missing MiKTeX and Pandoc components through winget.

## Source Route

Use this route:

```text
Markdown/content -> structured LaTeX .tex -> xelatex/lualatex/pdflatex -> PDF -> visual QA
```

For Markdown input, convert prose and headings manually when precision matters. Use Pandoc only if it is installed and the source structure is simple enough to preserve equations safely.

## CJK Technical Report Template

Use `ctexart` for Chinese/CJK reports:

```latex
\documentclass[UTF8,a4paper,12pt]{ctexart}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{amsmath,amssymb,bm,mathtools}
\usepackage{graphicx,booktabs,longtable,array}
\usepackage{hyperref}
\hypersetup{colorlinks=false,hidelinks}
\numberwithin{equation}{section}

\title{Title}
\author{Author}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\section{Section Title}
Text with inline math \(p\), \(\delta \mathbf{u}\), and \(\nabla \cdot \mathbf{u}\).

\begin{equation}
\nabla \cdot \boldsymbol{\sigma} + \rho \mathbf{b} = \mathbf{0}
\end{equation}

\begin{align}
\int_{\Omega}
\boldsymbol{\varepsilon}(\delta \mathbf{u})^T
\mathbf{D}
\boldsymbol{\varepsilon}(\mathbf{u})\,d\Omega
-
\int_{\Omega}
\alpha(\nabla \cdot \delta \mathbf{u})p\,d\Omega
&=
\int_{\Omega}
\delta \mathbf{u}^T \rho \mathbf{b}\,d\Omega \notag\\
&\quad+
\int_{\Gamma_t}
\delta \mathbf{u}^T \bar{\mathbf{t}}\,d\Gamma .
\end{align}

\end{document}
```

For Latin-only journal manuscripts, use the journal template or `article` with `amsmath`, `amssymb`, `bm`, and `mathtools`.

## Black Text Requirement

Unless the user or official journal template explicitly requires color, render everything in black: headings, subsection headings, body text, equation numbers, headers/footers, table rules, code/listing frames, citations, URLs, and internal links. In LaTeX, prefer `\hypersetup{colorlinks=false,hidelinks}` and avoid `\color{...}` in heading styles.

## Equation Rules

- Use inline math `\( ... \)` for short symbols and variables.
- Use `equation` for single displayed equations.
- Use `align` for multi-line derivations; align at relation symbols with `&`.
- Use `split` inside `equation` when a single numbered equation needs multiple lines.
- Use `bmatrix`, `pmatrix`, or `aligned` for matrix/vector systems.
- Use `\mathbf{u}` for vectors, `\boldsymbol{\sigma}` or `\bm{\sigma}` for Greek tensor symbols, and `\mathrm{d}` only if the target style requires upright differentials.
- Break long equations intentionally; do not let them overflow margins.
- Avoid equation images unless the user explicitly requests screenshot-style output.

## Compile

Run at least two passes for TOC and references:

```powershell
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

Or use the bundled helper:

```powershell
python scripts/compile_latex_pdf.py manuscript.tex --engine xelatex
```

If using BibTeX/Biber, run the bibliography tool between LaTeX passes.

## QA

Render or inspect the final PDF pages containing equations. Fix:

- missing glyphs or square boxes,
- raw LaTeX printed in the PDF,
- equation images where native equations were required,
- overfull equations crossing margins,
- clipped superscripts/subscripts,
- inconsistent numbering,
- bad CJK/Latin spacing around inline math.

Deliver the `.pdf` and `.tex` source. Include logs only when compilation warnings/errors matter.
