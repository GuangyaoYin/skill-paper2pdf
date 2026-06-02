# Toolchain Install Policy

Use this reference when the selected Paper2PDF route requires a missing local tool. Install only what is required for the requested output; do not install broad toolchains by habit.

## Decision Rules

- Standard mathematical equations in PDF: need a LaTeX engine. Prefer `xelatex` for Chinese/CJK or Unicode reports.
- Markdown-to-LaTeX conversion: need `pandoc` only if manual conversion is not preferable or the user explicitly wants Pandoc conversion.
- Existing `.tex` to PDF: need only a LaTeX engine.
- Latin-only simple LaTeX: `pdflatex`, `lualatex`, `xelatex`, or `tectonic` may work.
- CJK reports: prefer MiKTeX/TeX Live/TinyTeX with `xelatex` and CJK packages; `tectonic` may be insufficient for `ctexart` documents.

## Windows Default

On Windows, prefer MiKTeX for LaTeX because it provides `xelatex` and can install missing packages on demand.

Check first:

```powershell
Get-Command xelatex,pdflatex,lualatex,tectonic,pandoc -ErrorAction SilentlyContinue
```

Install only missing pieces:

```powershell
# Install LaTeX engine if no xelatex/lualatex/pdflatex is available
winget install -e --id MiKTeX.MiKTeX --accept-package-agreements --accept-source-agreements

# Install Pandoc only when Markdown/doc conversion needs it
winget install --source winget --exact --id JohnMacFarlane.Pandoc --accept-package-agreements --accept-source-agreements
```

Use the bundled helper when possible:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install_latex_toolchain.ps1 -NeedLatex
powershell -ExecutionPolicy Bypass -File scripts/install_latex_toolchain.ps1 -NeedLatex -NeedPandoc
```

After installation, refresh PATH for the current shell if necessary, then re-run the toolchain check. If commands are still missing, open a new shell or locate the installed binaries before continuing.

## macOS

Use Homebrew when available:

```bash
brew install --cask mactex-no-gui
brew install pandoc
```

For a smaller TeX distribution, install TinyTeX manually and ensure `xelatex` is on PATH.

## Linux

Use the system package manager. Debian/Ubuntu examples:

```bash
sudo apt-get update
sudo apt-get install -y texlive-xetex texlive-latex-extra texlive-lang-chinese latexmk
sudo apt-get install -y pandoc
```

Install `pandoc` only if conversion requires it.

## Installation QA

After installing, verify:

```powershell
xelatex --version
pandoc --version
```

For CJK math reports, compile a tiny `ctexart` smoke test before working on a long manuscript. If MiKTeX prompts to install missing packages, allow package installation.

## Failure Policy

If installation fails due to permissions, missing package manager, network failure, or an unavailable package ID, report the exact blocker. Do not fall back to formula images, ASCII formulas, or raw LaTeX text unless the user explicitly approves that lower-quality output.
