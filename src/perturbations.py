"""Helpers for working with frozen perturbation files.

The final study relies on frozen changed-query sets so every model is evaluated
on identical perturbed examples. Exact generation logic should remain in the
experiment notebooks until it is extracted and checked against the frozen files.
"""
from __future__ import annotations
import pandas as pd
REQUIRED_COLUMNS = {"condition", "original_text", "perturbed_text", "label"}

def load_perturbation_pairs(path):
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df

def changed_only(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[df["original_text"] != df["perturbed_text"]].copy()

def semantic_valid_only(df: pd.DataFrame, validity_column: str = "valid_semantics", valid_value: int = 1) -> pd.DataFrame:
    if validity_column not in df.columns:
        raise ValueError(f"{validity_column!r} not found in dataframe")
    return df.loc[pd.to_numeric(df[validity_column], errors="coerce") == valid_value].copy()
