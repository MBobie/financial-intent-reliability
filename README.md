# Financial Intent Reliability

**Calibration, robustness, selective prediction, and benchmark provenance for financial intent classification**

This repository supports the study:

> **Knowing When Not to Predict: Calibration, Robustness, and Selective Prediction for Financial Intent Classification**

The project evaluates whether financial intent classifiers can do more than produce accurate labels: it asks whether they remain reliable under realistic surface-form variation, whether their probabilities are calibrated, and whether their uncertainty scores can identify predictions that should be withheld.

## Study scope

The primary experiments use **Hilbot-FI** (1,525 English utterances, 33 intents) and compare four model families:

- TF-IDF Logistic Regression
- Sigmoid-calibrated Linear SVM
- Hybrid CNN + TF-IDF
- DistilBERT

External validation uses **BANKING77**.

The evaluation covers:

- clean predictive performance;
- probability calibration;
- selective prediction and abstention;
- typo, abbreviation, and query-shortening robustness;
- multi-seed neural training;
- Holm-corrected paired testing;
- paired bootstrap comparisons of degradation;
- semantic validity auditing of perturbations;
- benchmark provenance and train/test template overlap;
- source-stratified evaluation;
- external validation on BANKING77.

## Main findings

The final analysis supports five distinct reliability dimensions that should not be collapsed into one headline accuracy value:

1. **Predictive accuracy**
2. **Probability calibration**
3. **Perturbation robustness**
4. **Selective reliability / correctness ranking**
5. **Benchmark provenance**

A key provenance result is that **180 of 305 Hilbot-FI test queries (59.0%) have an exact numeric-normalized counterpart in training**. All four model families classify this template-matched partition perfectly, so aggregate accuracy mixes within-template performance with performance on non-template-matched queries.

Across three neural training seeds, the two neural models remain strong on clean data, but their robustness, calibration, and selective behavior differ. The analysis also shows that lower ECE under perturbation does not necessarily imply improved probability quality when proper scoring rules such as Brier score and NLL worsen.

## Repository structure

```text
financial-intent-reliability/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
├── CONTRIBUTING.md
│
├── notebooks/
│   ├── 01_hilbot_primary_experiments.ipynb
│   ├── 02_banking77_external_validation.ipynb
│   └── 03_reviewer_hardening.ipynb
│
├── src/
│   ├── __init__.py
│   ├── metrics.py
│   ├── evaluation.py
│   └── perturbations.py
│
├── data/
│   ├── README.md
│   ├── splits/
│   │   └── README.md
│   └── perturbations/
│       └── README.md
│
├── audit/
│   └── README.md
│
├── results/
│   ├── tables/
│   │   └── README.md
│   └── figures/
│       └── README.md
│
├── paper/
│   └── README.md
│
└── docs/
    ├── REPRODUCIBILITY.md
    ├── DATA_STATEMENT.md
    └── RELEASE_CHECKLIST.md
```

## Notebook order

Run the notebooks in this order:

1. `01_hilbot_primary_experiments.ipynb`
2. `02_banking77_external_validation.ipynb`
3. `03_reviewer_hardening.ipynb`

The third notebook performs the final reviewer-hardening analyses, including multi-seed neural evaluation, provenance analysis, multiplicity correction, paired bootstrap comparisons, perturbation calibration, source stratification, and semantic-audit sensitivity analysis.

## Quick start

Create a clean Python environment and install dependencies:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) before running the experiments.

## Data availability

This repository should **not redistribute raw Hilbot-FI or third-party datasets unless redistribution permission is confirmed**.

The `data/` directory is intended for:

- split identifiers;
- frozen changed-query lists;
- derived perturbation files that may legally be shared;
- instructions for obtaining source datasets.

See [`docs/DATA_STATEMENT.md`](docs/DATA_STATEMENT.md).

## Reproducibility

The repository is designed to preserve:

- the fixed train/test split;
- fixed neural validation indices;
- frozen perturbation sets;
- neural training seeds `{42, 123, 2026}`;
- the semantic perturbation audit;
- benchmark provenance analysis;
- paper-ready result tables.

Important: do not commit model checkpoints, downloaded transformer caches, full GloVe files, access tokens, secrets, or private cloud paths.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Replace the placeholder author names before making the repository public.

## License

The code scaffold is distributed under the MIT License. Dataset files are **not automatically covered by the code license** and remain subject to their original terms.

## Research status

This repository accompanies an academic manuscript in preparation/submission. Repository contents should be treated as research software and experimental materials rather than a production financial decision system.
