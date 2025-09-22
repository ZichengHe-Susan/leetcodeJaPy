from typing import List, Tuple


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        return 0


def _run_sample_tests() -> None:
    tests: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1], 1, 2),
        ([5, 5, 5, 5], 2, 2),
    ]

    solver = Solution()
    passed = 0
    for idx, (nums, k, expected) in enumerate(tests, 1):
        got = solver.maxSubarrayLength(nums, k)
        if got == expected:
            print(f"[PASS] Test {idx}: got={got}, expected={expected}")
            passed += 1
        else:
            print(f"[FAIL] Test {idx}: got={got}, expected={expected}, input=nums={nums}, k={k}")

    print(f"\nPublic tests: {passed}/{len(tests)} passed")


if __name__ == "__main__":
    _run_sample_tests()


