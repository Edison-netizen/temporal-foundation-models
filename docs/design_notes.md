# Design Notes

Temporal foundation models are easy to overclaim. The first goal is to make transfer claims testable.

## Minimal Evaluation Matrix

| Pretraining | Forecasting | Classification | Anomaly Detection |
|---|---|---|---|
| none | baseline | baseline | baseline |
| masked points | compare | compare | compare |
| masked patches | compare | compare | compare |
| masked variables | compare | compare | compare |

## Risks

- Dataset leakage through normalization.
- Transfer claims based on one target dataset.
- Context length gains confused with pretraining gains.
- Metric improvements concentrated in short horizons only.

