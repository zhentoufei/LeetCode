package easy;

public class Rob {

	private static int[] memo;

	private static int try_rob(int[] n, int index) {
		if (index >= n.length)
			return 0;

		if (memo[index] != -1)
			return memo[index];
		int res = 0;
		for (int i = index; i < n.length; i++) {
			res = Math.max(res, n[i] + try_rob(n, i + 2));
		}
		memo[index] = res;
		return res;

	}

	public static int rob(int[] n) {
		memo = new int[n.length];
		for (int i = 0; i < n.length; i++) {
			memo[i] = -1;
		}
		return try_rob(n, 0);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = { 1, 2, 3, 4, 5 };
		System.out.print(rob(arr));

	}

}
