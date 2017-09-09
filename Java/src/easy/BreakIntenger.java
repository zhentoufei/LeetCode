package easy;

import java.util.ArrayList;
import java.util.List;

public class BreakIntenger {

	private static List<Integer> memo = new ArrayList<>();

	private static int max_3(int a, int b, int c) {
		return Math.max(Math.max(a, b), c);
	}

	private static int BreakINtenger(int n) {

		if (n == 1) {
			return 1;
		}
		if (memo.get(n) != -1) {
			return memo.get(n);
		}
		int res = -1;
		for (int i = 1; i <= n - 1; i++) {
			res = max_3(res, i * (n - i), i * BreakINtenger(n - i));
		}
		memo.set(n, res);
		return res;

	}

	public static int IntBreaker(int n) {
		for (int i = 0; i < n + 1; i++) {
			memo.add(-1);
		}
		return BreakINtenger(n);

	}

	public static int IntBreakerInDP(int n) {
		if (n < 2) {
			return 0;
		}
		Integer[] memo_dp = new Integer[n + 1];
		for (int i = 0; i <= n; i++) {
			memo_dp[i] = -1;
		}
		memo_dp[1] = 1;
		for (int i = 2; i <= n; i++) {
			for (int j = 1; j <= i - 1; j++) {
				memo_dp[i] = max_3(memo_dp[i], j * (i - j), j * memo_dp[i - j]);
			}
		}
		return memo_dp[n];

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(IntBreakerInDP(5));
	}

}
