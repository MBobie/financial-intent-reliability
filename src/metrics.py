"""Shared metrics for calibration and selective prediction."""
from __future__ import annotations
import numpy as np
from sklearn.metrics import log_loss, roc_auc_score

def top2_margin(probs: np.ndarray) -> np.ndarray:
    probs = np.asarray(probs, dtype=float)
    if probs.ndim != 2 or probs.shape[1] < 2:
        raise ValueError("probs must have shape (n_samples, n_classes>=2)")
    part = np.partition(probs, -2, axis=1)
    return part[:, -1] - part[:, -2]

def max_probability(probs: np.ndarray) -> np.ndarray:
    probs = np.asarray(probs, dtype=float)
    return np.max(probs, axis=1)

def predictive_entropy(probs: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    probs = np.asarray(probs, dtype=float)
    probs = np.clip(probs, eps, 1.0)
    return -(probs * np.log(probs)).sum(axis=1)

def multiclass_brier_score(y_true: np.ndarray, probs: np.ndarray, n_classes: int | None = None) -> float:
    y_true = np.asarray(y_true, dtype=int)
    probs = np.asarray(probs, dtype=float)
    if n_classes is None:
        n_classes = probs.shape[1]
    one_hot = np.eye(n_classes, dtype=float)[y_true]
    return float(np.mean(np.sum((probs - one_hot) ** 2, axis=1)))

def expected_calibration_error(y_true: np.ndarray, probs: np.ndarray, n_bins: int = 10) -> float:
    y_true = np.asarray(y_true)
    probs = np.asarray(probs, dtype=float)
    pred = probs.argmax(axis=1)
    conf = probs.max(axis=1)
    correct = (pred == y_true).astype(float)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        lo, hi = edges[i], edges[i + 1]
        mask = (conf >= lo) & ((conf <= hi) if i == n_bins - 1 else (conf < hi))
        if not np.any(mask):
            continue
        ece += mask.mean() * abs(correct[mask].mean() - conf[mask].mean())
    return float(ece)

def negative_log_likelihood(y_true: np.ndarray, probs: np.ndarray) -> float:
    return float(log_loss(y_true, probs, labels=np.arange(probs.shape[1])))

def correctness_auroc(correct: np.ndarray, score: np.ndarray) -> float:
    correct = np.asarray(correct, dtype=int)
    score = np.asarray(score, dtype=float)
    if np.unique(correct).size < 2:
        return float("nan")
    return float(roc_auc_score(correct, score))

def risk_coverage_curve(correct: np.ndarray, score: np.ndarray):
    correct = np.asarray(correct, dtype=bool)
    score = np.asarray(score, dtype=float)
    if correct.shape[0] != score.shape[0]:
        raise ValueError("correct and score must have the same length")
    order = np.argsort(-score, kind="mergesort")
    ordered_correct = correct[order].astype(float)
    n = len(ordered_correct)
    if n == 0:
        return np.array([]), np.array([])
    cumulative_accuracy = np.cumsum(ordered_correct) / np.arange(1, n + 1)
    risk = 1.0 - cumulative_accuracy
    coverage = np.arange(1, n + 1) / n
    return coverage, risk

def aurc_from_score(correct: np.ndarray, score: np.ndarray) -> float:
    coverage, risk = risk_coverage_curve(correct, score)
    if len(coverage) == 0:
        return float("nan")
    coverage = np.concatenate([[0.0], coverage])
    risk = np.concatenate([[risk[0]], risk])
    return float(np.trapz(risk, coverage))
