from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
import logging

def evaluate_model(y_true, y_pred, label):
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_pred),
    }
    logging.info(f"{label} Metrics: {metrics}")
    return metrics
