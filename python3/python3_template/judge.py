from typing import List, Tuple
from solution import Solution


def run_full_judge() -> None:
    public_tests: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1], 1, 2),
        ([5, 5, 5, 5], 2, 2),
    ]

    hidden_tests: List[Tuple[List[int], int, int]] = [
        ([1, 1, 1, 2, 2, 3], 2, 5),
        ([1, 2, 3, 4, 5], 1, 5),
        ([2, 2, 2, 2, 2, 2, 2], 3, 3),
    ]

    tests = public_tests + hidden_tests
    solver = Solution()
    passed = 0
    for idx, (nums, k, expected) in enumerate(tests, 1):
        got = solver.maxSubarrayLength(nums, k)
        ok = got == expected
        if ok:
            print(f"[PASS] Test {idx}: got={got}, expected={expected}")
            passed += 1
        else:
            print(f"[FAIL] Test {idx}: got={got}, expected={expected}, input=nums={nums}, k={k}")

    print(f"\nJudge: {passed}/{len(tests)} passed")


if __name__ == "__main__":
    run_full_judge()


