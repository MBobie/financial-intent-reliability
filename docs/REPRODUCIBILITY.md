# Reproducibility Guide

## 1. Environment

Reference versions used in the final reviewer-hardening workflow included:

- TensorFlow 2.20.0
- PyTorch 2.11.0
- Transformers 5.13.1

Exact bitwise reproduction is not guaranteed across hardware and library builds, especially for neural fine-tuning. The manuscript therefore reports neural results across three seeds descriptively.

## 2. Fixed experimental components

Keep fixed across reruns:

- Hilbot-FI train/test split
- neural train/validation indices
- TF-IDF vocabulary fitting protocol
- frozen perturbation sets
- changed-query membership for each perturbation condition

Neural training seeds:

```text
42
123
2026
```

## 3. Recommended execution order

```text
01_hilbot_primary_experiments.ipynb
02_banking77_external_validation.ipynb
03_reviewer_hardening.ipynb
```

## 4. Primary uncertainty score

Top-2 probability margin is used uniformly as the primary cross-model selective score. Maximum probability and negative entropy are secondary diagnostics.

## 5. Calibration metrics

The manuscript reports ECE with 10 equal-width bins, multiclass Brier score, and negative log likelihood.

Do not interpret ECE alone under perturbation. An ECE reduction can occur even when Brier score and NLL worsen.

## 6. Statistical analysis

Primary perturbation family:

```text
4 models × 3 perturbations = 12 paired accuracy tests
```

These are corrected using Holm's step-down procedure. Secondary uncertainty tests form a separate family. Between-model degradation is evaluated using paired bootstrap confidence intervals on identical queries.

## 7. Semantic audit

The reviewed perturbation audit contains 322 pairs: 106 abbreviation, 116 shortening, and 100 sampled typo. Final judgments are 319 clearly intent-preserving, 3 uncertain, and 0 clearly label-changing.

## 8. Provenance audit

Numeric-normalized matching replaces numeric expressions with a common marker and normalizes case, non-alphabetic formatting, and whitespace. No month names, category names, or other lexical slots should be replaced unless that is explicitly implemented and separately reported.

## 9. What not to commit

Do not commit model checkpoints, Hugging Face cache files, full GloVe downloads, credentials/tokens, private cloud paths, or raw third-party datasets without redistribution permission.
