package easy;

public class Knapsack01_in_DP {

	private static int[][] memo;

	private static int find_best_value(int[] weights, int[] values, int c) {
		int len_weights = weights.length;
		if (len_weights == 0)
			return 0;
		memo = new int[len_weights][c + 1];
		for (int i = 0; i < len_weights; i++)
			for (int j = 0; j < c + 1; j++) {
				memo[i][j] = -1;
			}

		for (int i = 0; i <= c; i++)
			memo[0][i] = (i >= weights[0] ? values[0] : 0);

		for (int i = 1; i < len_weights; i++)
			for (int j = 0; j <= c; j++) {
				memo[i][j] = memo[i - 1][j];
				if (j >= weights[i])
					memo[i][j] = Math.max(memo[i][j], values[i] + memo[i - 1][j - weights[i]]);
			}

		return memo[len_weights - 1][c];
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
