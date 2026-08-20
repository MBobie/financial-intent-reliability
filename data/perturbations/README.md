# Frozen perturbation files

Place the final query-pair files used for evaluation here.

Recommended files:

```text
hilbot_typo_pairs.csv
hilbot_abbreviation_pairs.csv
hilbot_shortening_pairs.csv
banking77_typo_pairs.csv
```

Recommended columns:

```text
row_id
condition
original_text
perturbed_text
label
source
```

If semantic-audit labels are included, add `valid_semantics` and `review_notes`.

Do not regenerate these files silently after manuscript results have been finalized.
