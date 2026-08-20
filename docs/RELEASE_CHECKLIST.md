# Public Release Checklist

## Repository hygiene

- [ ] Notebook filenames are final
- [ ] Debug cells and temporary outputs are removed
- [ ] No private Google Drive paths remain unless necessary and documented
- [ ] No API keys, access tokens, passwords, or credentials are present
- [ ] No model checkpoints or caches are committed
- [ ] No full GloVe file is committed
- [ ] `.gitignore` is active

## Data

- [ ] Raw Hilbot-FI redistribution rights have been checked
- [ ] BANKING77 is linked rather than unnecessarily copied
- [ ] Split identifiers are included
- [ ] Frozen perturbation files are included if legally shareable
- [ ] Semantic-audit file is included
- [ ] Provenance-audit outputs are included

## Results

- [ ] Final CSV tables match the manuscript
- [ ] Reliability diagram is the final version
- [ ] Risk-coverage figure is the final version
- [ ] Single-seed figures are clearly labelled as such

## Metadata

- [ ] README is accurate
- [ ] `CITATION.cff` author names are filled in
- [ ] GitHub URL is filled in
- [ ] LICENSE author line is filled in
- [ ] Repository version/tag is chosen

## Publication

- [ ] No journal/conference policy is violated by public release
- [ ] Preprint status is labelled correctly
- [ ] Code Availability statement in the manuscript matches the repository
- [ ] Repository DOI is added later if archived with Zenodo
