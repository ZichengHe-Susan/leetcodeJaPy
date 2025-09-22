import java.util.Arrays;

public class TestRunner {
    private static class TestCase {
        int[] nums;
        int k;
        int expected;
        TestCase(int[] nums, int k, int expected) {
            this.nums = nums;
            this.k = k;
            this.expected = expected;
        }
    }

    public static void main(String[] args) {
        TestCase[] tests = new TestCase[] {
            new TestCase(new int[] {1,2,3,1,2,3,1,2}, 2, 6),
            new TestCase(new int[] {1,2,1,2,1,2,1}, 1, 2),
            new TestCase(new int[] {5,5,5,5}, 2, 2),
        };

        Solution solver = new Solution();
        int passed = 0;
        for (int i = 0; i < tests.length; i++) {
            TestCase t = tests[i];
            int got = solver.maxSubarrayLength(t.nums, t.k);
            boolean ok = got == t.expected;
            if (ok) {
                System.out.printf("[PASS] Test %d: got=%d, expected=%d%n", i + 1, got, t.expected);
                passed++;
            } else {
                System.out.printf("[FAIL] Test %d: got=%d, expected=%d, input=nums=%s, k=%d%n",
                    i + 1, got, t.expected, Arrays.toString(t.nums), t.k);
            }
        }
        System.out.printf("%nPublic tests: %d/%d passed%n", passed, tests.length);
    }
}


