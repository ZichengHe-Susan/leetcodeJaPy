## LeetCode-style Local Templates (Python3 and Java)

This repo provides runnable skeletons for solving LeetCode-style problems locally in Python and Java. Each template includes:

- `Solution` class with the required signature
- Embedded public tests inside the solution file (quick feedback)
- Judge runner with public + hidden tests (simulate full submission)

### Python (python3/python3_template)

Files:
- `solution.py`: implement `Solution.maxSubarrayLength(self, nums: List[int], k: int) -> int`. Contains embedded public tests and a `__main__` entrypoint.
- `judge.py`: runs public + hidden tests.
- `run_solution.sh`, `judge.sh`: convenience scripts.

Run embedded public tests:
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/python3/python3_template/run_solution.sh
# or directly
python3 /Users/hebaqi/Desktop/UVA/Career/leetcode/python3/python3_template/solution.py
```

Run judge (public + hidden):
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/python3/python3_template/judge.sh
```

### Java (java/java_template)

Files:
- `src/Solution.java`: implement `public int maxSubarrayLength(int[] nums, int k)`. Contains a `main` method with embedded public tests.
- `src/Judge.java`: runs public + hidden tests.
- `build.sh`, `run_solution.sh`, `judge.sh`.

Run embedded public tests:
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/run_solution.sh
# or directly
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/build.sh && \
java -cp /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/out Solution
```

Run judge (public + hidden):
```bash
sh /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/judge.sh
```

Notes:
- The sample expected outputs are placeholders. Update `expected` once you implement the real logic.
- You can replace tests with ones matching your current LeetCode problem.

### Make scripts executable (first time only)

If you see `permission denied` when running a `.sh` file, grant execute permission once:

```bash
chmod +x /Users/hebaqi/Desktop/UVA/Career/leetcode/python3/python3_template/run_solution.sh
chmod +x /Users/hebaqi/Desktop/UVA/Career/leetcode/python3/python3_template/judge.sh

chmod +x /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/build.sh
chmod +x /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/run_solution.sh
chmod +x /Users/hebaqi/Desktop/UVA/Career/leetcode/java/java_template/judge.sh
```


