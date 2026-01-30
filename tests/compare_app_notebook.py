import os
import joblib
import numpy as np


def load_rf():
    models_dir = os.path.join(os.path.dirname(__file__), "..", "models")
    rf_path = os.path.join(models_dir, "random_forest.pkl")
    return joblib.load(rf_path)


def run_examples(rf):
    examples = [
        ("Low risk (typical)", [0, 85, 66, 29, 0, 26.6, 0.351, 31]),
        ("Medium risk", [2, 120, 70, 20, 79, 28.0, 0.5, 45]),
        ("High glucose/age", [4, 180, 85, 25, 200, 35.0, 1.2, 55]),
    ]

    results = []
    for name, vals in examples:
        X = np.array(vals).reshape(1, -1)
        prob = rf.predict_proba(X)[0, 1]
        pred = int(rf.predict(X)[0])
        results.append((name, prob, pred))

    return results


def main():
    rf = load_rf()
    results = run_examples(rf)

    print("Example predictions from Random Forest:")
    for name, prob, pred in results:
        print(f"{name}: probability={prob:.4f}, class={pred}")


if __name__ == "__main__":
    main()
