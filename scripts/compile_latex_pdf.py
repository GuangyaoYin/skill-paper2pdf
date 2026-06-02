#!/usr/bin/env python3
"""Compile a LaTeX manuscript to PDF with a suitable engine."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ENGINES = ("xelatex", "lualatex", "pdflatex", "tectonic")


def choose_engine(requested: str | None) -> str:
    if requested:
        if shutil.which(requested):
            return requested
        raise SystemExit(f"Requested LaTeX engine is not installed: {requested}")
    for engine in ENGINES:
        if shutil.which(engine):
            return engine
    raise SystemExit(
        "No LaTeX engine found. Install TinyTeX, TeX Live, or MiKTeX "
        "(need one of: xelatex, lualatex, pdflatex, tectonic)."
    )


def run(cmd: list[str], cwd: Path) -> None:
    print("+ " + " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, cwd=str(cwd), text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def compile_tex(tex: Path, engine: str, passes: int) -> Path:
    tex = tex.resolve()
    if not tex.exists():
        raise SystemExit(f"TeX source not found: {tex}")
    cwd = tex.parent
    if engine == "tectonic":
        run(["tectonic", str(tex.name)], cwd)
    else:
        cmd = [engine, "-interaction=nonstopmode", "-halt-on-error", tex.name]
        for _ in range(max(1, passes)):
            run(cmd, cwd)
    pdf = tex.with_suffix(".pdf")
    if not pdf.exists():
        raise SystemExit(f"Compilation finished but PDF was not created: {pdf}")
    return pdf


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", help="Path to .tex manuscript")
    parser.add_argument("--engine", choices=ENGINES, help="LaTeX engine to use")
    parser.add_argument("--passes", type=int, default=2, help="Compile passes for TOC/references")
    args = parser.parse_args(argv)

    engine = choose_engine(args.engine)
    pdf = compile_tex(Path(args.tex), engine, args.passes)
    print(f"Done: {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
