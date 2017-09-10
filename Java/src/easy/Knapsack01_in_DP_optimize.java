package easy;

public class Knapsack01_in_DP_optimize {

	private static int[][] memo;

	private static int find_best_value(int[] weights, int[] values, int c) {
		int len_weights = weights.length;
		if (len_weights == 0)
			return 0;
		memo = new int[2][c + 1];
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < c + 1; j++) {
				memo[i][j] = -1;
			}

		for (int i = 0; i <= c; i++)
			memo[0][i] = (i >= weights[0] ? values[0] : 0);

		for (int i = 1; i < len_weights; i++)
			for (int j = 0; j <= c; j++) {
				memo[i % 2][j] = memo[(i - 1) % 2][j];
				if (j >= weights[i])
					memo[i % 2][j] = Math.max(memo[i % 2][j], values[i] + memo[(i - 1) % 2][j - weights[i]]);
			}

		return memo[(len_weights - 1) % 2][c];
	}

	public static int knapsack01(int[] weights, int[] values, int C) {
		return find_best_value(weights, values, C);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] weights = { 1, 2, 3 };
		int[] value = { 6, 10, 12 };
		int C = 5;
		System.out.println(knapsack01(weights, value, C));

	}

}
