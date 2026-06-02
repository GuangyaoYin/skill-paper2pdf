param(
    [switch]$NeedLatex,
    [switch]$NeedPandoc
)

$ErrorActionPreference = "Stop"

function Has-Command($Name) {
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Require-Winget {
    if (-not (Has-Command "winget")) {
        throw "winget is not available. Install App Installer / Windows Package Manager, or install MiKTeX/Pandoc manually."
    }
}

function Install-WingetPackage($Id, $Label) {
    Require-Winget
    Write-Host "Installing $Label ($Id) via winget..."
    winget install --source winget --exact --id $Id --accept-package-agreements --accept-source-agreements
}

$hasLatex = (Has-Command "xelatex") -or (Has-Command "lualatex") -or (Has-Command "pdflatex") -or (Has-Command "tectonic")

if ($NeedLatex -and -not $hasLatex) {
    Install-WingetPackage "MiKTeX.MiKTeX" "MiKTeX"
} elseif ($NeedLatex) {
    Write-Host "LaTeX engine already available."
}

if ($NeedPandoc -and -not (Has-Command "pandoc")) {
    Install-WingetPackage "JohnMacFarlane.Pandoc" "Pandoc"
} elseif ($NeedPandoc) {
    Write-Host "Pandoc already available."
}

Write-Host "Toolchain check:"
Get-Command xelatex,pdflatex,lualatex,tectonic,pandoc -ErrorAction SilentlyContinue | Select-Object Name,Source
