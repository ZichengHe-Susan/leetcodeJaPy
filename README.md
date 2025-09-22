## LeetCode-style Local Templates (Python3 and Java)

This repo provides runnable skeletons for solving LeetCode-style problems locally in Python and Java. Each template includes:

- `Solution` class with the required signature
- Public tests runner (quick feedback)
- Judge runner with public + hidden tests (simulate full submission)

### Python (python3_template)

Files:
- `solution.py`: implement `Solution.maxSubarrayLength(self, nums: List[int], k: int) -> int`
- `run_tests.py`: runs 1-3 public tests
- `judge.py`: runs public + hidden tests
- `run_tests.sh`, `judge.sh`: convenience scripts

Run:
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/python3_template/run_tests.sh
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/python3_template/judge.sh
```

### Java (java_template)

Files:
- `src/Solution.java`: implement `public int maxSubarrayLength(int[] nums, int k)`
- `src/TestRunner.java`: runs 1-3 public tests
- `src/Judge.java`: runs public + hidden tests
- `build.sh`, `run_tests.sh`, `judge.sh`

Build and run:
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/java_template/run_tests.sh
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/java_template/judge.sh
```

Notes:
- The sample expected outputs are placeholders. Update `expected` once you implement the real logic.
- You can replace tests with ones matching your current LeetCode problem.


