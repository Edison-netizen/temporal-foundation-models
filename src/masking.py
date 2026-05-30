from __future__ import annotations

import random
from typing import Sequence


def masked_patch_indices(num_steps: int, patch_len: int, mask_ratio: float, seed: int = 42) -> list[int]:
    """Return patch start indices selected for masked temporal modeling."""
    if patch_len <= 0:
        raise ValueError("patch_len must be positive")
    if not 0 <= mask_ratio <= 1:
        raise ValueError("mask_ratio must be in [0, 1]")

    starts = list(range(0, num_steps - patch_len + 1, patch_len))
    k = round(len(starts) * mask_ratio)
    rng = random.Random(seed)
    return sorted(rng.sample(starts, k))


def expand_patch_mask(starts: Sequence[int], patch_len: int, num_steps: int) -> list[bool]:
    mask = [False] * num_steps
    for start in starts:
        for idx in range(start, min(start + patch_len, num_steps)):
            mask[idx] = True
    return mask

