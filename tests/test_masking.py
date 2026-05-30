from masking import expand_patch_mask, masked_patch_indices


def test_masked_patch_indices_are_deterministic():
    first = masked_patch_indices(num_steps=64, patch_len=8, mask_ratio=0.25, seed=7)
    second = masked_patch_indices(num_steps=64, patch_len=8, mask_ratio=0.25, seed=7)

    assert first == second
    assert len(first) == 2


def test_expand_patch_mask_marks_expected_span():
    mask = expand_patch_mask([4], patch_len=3, num_steps=10)

    assert mask == [False, False, False, False, True, True, True, False, False, False]

