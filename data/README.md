# Data

Do not place raw datasets here unless you have confirmed that redistribution is allowed.

Recommended contents:

```text
data/
├── README.md
├── splits/
│   ├── hilbot_train_ids.csv
│   ├── hilbot_test_ids.csv
│   └── hilbot_validation_ids.csv
└── perturbations/
    ├── hilbot_typo_pairs.csv
    ├── hilbot_abbreviation_pairs.csv
    └── hilbot_shortening_pairs.csv
```

The preferred reproducibility strategy is to publish split identifiers, frozen perturbation pairs, instructions for obtaining the original dataset, and scripts/notebooks that reconstruct derived outputs.

Do not commit personally identifying information, credentials, or any dataset copy whose license does not permit redistribution.
