package easy;

public class Knapsack01 {

	private static int[][] memo;

	private static int find_bset_values(int[] weitghts, int[] values, int index, int c) {
		if (index < 0 || c <= 0) {
			return 0;
		}

		if (memo[index][c] != -1)
			return memo[index][c];

		// ���ַ�ʽ���õ���õĶ���
		// ��һ�֣���ǰ��ֵ��Ϊ��õģ�����Ҫȡ��ǰ����Ʒ���Ž�����
		// �ڶ��֣���ǰ����+֮ǰindex-1����Сֵ

		int res = find_bset_values(weitghts, values, index - 1, c);
		if (c >= weitghts[index])
			res = Math.max(res, values[index] + find_bset_values(weitghts, values, index - 1, c - weitghts[index]));
		memo[index][c] = res;
		return res;
	}

	public static int knapsack01(int[] weights, int[] values, int C) {
		int len_weights = weights.length;
		memo = new int[len_weights][C + 1];
		for (int i = 0; i < len_weights; i++) {
			for (int j = 0; j <= C; j++) {
				memo[i][j] = -1;
			}
		}
		return find_bset_values(weights, values, len_weights - 1, C);
	}

	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
		int[] weights = { 1, 2, 3 };
		int[] value = { 6, 10, 12 };
		int C = 5;
		System.out.println(knapsack01(weights, value, C));
	}

}
