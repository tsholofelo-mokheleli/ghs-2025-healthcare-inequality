
from pathlib import Path

ROOT = Path(__file__).resolve().parent

folders = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src",
    "config",
    "docs/official",
    "outputs/figures",
    "outputs/tables",
    "outputs/audit",
    "outputs/models",
    "outputs/manuscript",
    "tests",
]

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "src/__init__.py",
    "config/analysis_config.yaml",
    "docs/analysis_decisions.md",
    "notebooks/01_data_preparation.ipynb",
    "notebooks/02_descriptive_inequalities.ipynb",
    "notebooks/03_statistical_modelling.ipynb",
    "notebooks/04_moderation_vulnerability.ipynb",
    "notebooks/05_robustness_publication.ipynb",
]

for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

for filename in files:
    path = ROOT / filename

    if not path.exists():
        if path.suffix == ".ipynb":
            import json

            notebook = {
                "cells": [],
                "metadata": {
                    "kernelspec": {
                        "display_name": "Python 3",
                        "language": "python",
                        "name": "python3"
                    }
                },
                "nbformat": 4,
                "nbformat_minor": 5
            }

            path.write_text(
                json.dumps(notebook, indent=2),
                encoding="utf-8"
            )
        else:
            path.touch()

print("GHS 2025 project structure created successfully!")
