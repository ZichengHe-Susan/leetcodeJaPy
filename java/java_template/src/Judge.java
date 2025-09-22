import java.util.Arrays;

public class Judge {
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
        TestCase[] publicTests = new TestCase[] {
            new TestCase(new int[] {1,2,3,1,2,3,1,2}, 2, 6),
            new TestCase(new int[] {1,2,1,2,1,2,1}, 1, 2),
            new TestCase(new int[] {5,5,5,5}, 2, 2),
        };

        TestCase[] hiddenTests = new TestCase[] {
            new TestCase(new int[] {1,1,1,2,2,3}, 2, 5),
            new TestCase(new int[] {1,2,3,4,5}, 1, 5),
            new TestCase(new int[] {2,2,2,2,2,2,2}, 3, 3),
        };

        TestCase[] tests = concat(publicTests, hiddenTests);

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
        System.out.printf("%nJudge: %d/%d passed%n", passed, tests.length);
    }

    private static TestCase[] concat(TestCase[] a, TestCase[] b) {
        TestCase[] out = new TestCase[a.length + b.length];
        System.arraycopy(a, 0, out, 0, a.length);
        System.arraycopy(b, 0, out, a.length, b.length);
        return out;
    }
}


