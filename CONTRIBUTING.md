# Contributing

This repository primarily serves as a reproducibility package for an academic study.

## Before contributing

Please open an issue describing:

- the proposed change;
- whether it affects numerical results;
- whether it changes dataset handling;
- whether it changes the experimental protocol.

## Reproducibility-sensitive changes

Changes to any of the following should be clearly documented:

- train/test split identifiers;
- validation indices;
- perturbation generation or frozen perturbation files;
- model hyperparameters;
- random seeds;
- metric definitions;
- statistical testing;
- provenance normalization rules.

Do not silently replace an experimental artifact used in the manuscript.

## Data and privacy

Do not commit:

- private user data;
- credentials or tokens;
- copyrighted datasets without redistribution permission;
- model caches or downloaded third-party artifacts that should instead be obtained from their original source.
