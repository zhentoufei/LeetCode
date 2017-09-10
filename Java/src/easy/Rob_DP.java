package easy;

public class Rob_DP {

	public static int rob_1(int[] nums) {
		int length_nums = nums.length;
		if (length_nums == 0)
			return 0;

		int[] memo = new int[length_nums];
		for (int i = 0; i < length_nums; i++) {
			memo[i] = -1;
		}

		memo[length_nums - 1] = nums[length_nums - 1];
		for (int i = length_nums - 2; i >= 0; i--) {
			for (int j = i; j <= length_nums - 1; j++)
				memo[i] = Math.max(memo[i], nums[i] + (j + 2 < length_nums ? memo[j + 2] : 0));
		}
		return memo[0];
	}

	public static int rob_2(int[] nums) {
		int length_nums = nums.length;
		if (length_nums == 0) {
			return 0;
		}
		int[] memo = new int[length_nums];
		for (int i = 0; i < length_nums; i++) {
			memo[i] = -1;
		}

		memo[0] = nums[0];
		for (int i = 1; i <= length_nums - 1; i++) {
			for (int j = 0; j <= i; j++) {
				memo[i] = Math.max(memo[i], nums[j] + (j - 2 >= 0 ? memo[j - 2] : 0));
			}
		}
		return memo[length_nums - 1];

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = { 1, 2, 3, 4, 5 };
		System.out.println(rob_1(arr));
		System.out.println(rob_2(arr));
	}

}
