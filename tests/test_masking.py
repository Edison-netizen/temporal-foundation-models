import unittest
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from masking import expand_patch_mask, masked_patch_indices


class MaskingTests(unittest.TestCase):
    def test_masked_patch_indices_are_deterministic(self):
        first = masked_patch_indices(num_steps=64, patch_len=8, mask_ratio=0.25, seed=7)
        second = masked_patch_indices(num_steps=64, patch_len=8, mask_ratio=0.25, seed=7)

        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)

    def test_expand_patch_mask_marks_expected_span(self):
        mask = expand_patch_mask([4], patch_len=3, num_steps=10)

        self.assertEqual(mask, [False, False, False, False, True, True, True, False, False, False])


if __name__ == "__main__":
    unittest.main()
