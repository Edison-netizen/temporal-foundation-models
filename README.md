# Temporal Foundation Models

Small utilities and notes around pretraining ideas for temporal data.

This is not a released foundation model. It is a scratchpad for making the design space concrete: masking strategies, context length, channel mixing, sampling-rate mismatch, and transfer evaluation.

## Questions

1. What should be masked: points, spans, patches, variables, or frequency bands?
2. Which pretext objective survives dataset shift?
3. How much temporal resolution can be compressed before downstream accuracy collapses?
4. Does a pretrained encoder help forecasting, classification, and anomaly detection together?

## Planned Components

```text
configs/pretrain.yaml     pretraining configuration sketch
src/masking.py            span and patch masking utilities
docs/design_notes.md      research design notes
```

## Current Position

Small, controlled experiments before large-scale claims.
