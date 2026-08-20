"""Convenience functions for evaluating one classifier output."""
from __future__ import annotations
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from .metrics import (aurc_from_score, correctness_auroc, expected_calibration_error,
                      max_probability, multiclass_brier_score, negative_log_likelihood,
                      predictive_entropy, top2_margin)

def evaluate_probabilities(y_true, probs):
    y_true = np.asarray(y_true)
    probs = np.asarray(probs, dtype=float)
    y_pred = probs.argmax(axis=1)
    correct = y_pred == y_true
    margin = top2_margin(probs)
    maxprob = max_probability(probs)
    neg_entropy = -predictive_entropy(probs)
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro")),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted")),
        "ece": expected_calibration_error(y_true, probs, n_bins=10),
        "brier": multiclass_brier_score(y_true, probs),
        "nll": negative_log_likelihood(y_true, probs),
        "margin_auroc": correctness_auroc(correct, margin),
        "margin_aurc": aurc_from_score(correct, margin),
        "maxprob_auroc": correctness_auroc(correct, maxprob),
        "entropy_auroc": correctness_auroc(correct, neg_entropy),
    }
