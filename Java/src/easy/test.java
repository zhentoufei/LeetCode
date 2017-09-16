package easy;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class test {

	private static List<ArrayList<Integer>> result_list = new ArrayList<ArrayList<Integer>>();
	private static Boolean[] used;

	private static void gen_permutation(int[] nums, int index, ArrayList<Integer> res) {

		// 终止条件
		if (index == nums.length) {
			// 保存
			result_list.add(res);
			return;
		}

		for (int i = 0; i < nums.length; i++) {
			// 先判断是否被使用了
			if (!used[i]) {
				used[i] = true;
				res.add(nums[i]);
				gen_permutation(nums, index + 1, res);
				res.remove(res.size()-1);
				used[i] = false;
			}
		}
		return;

	}

	public static List<ArrayList<Integer>> my_permutation(int[] nums) {

		result_list.clear();
		if (nums.length == 0)
			return result_list;

		used = new Boolean[nums.length];
		Arrays.fill(used, false);
		ArrayList<Integer> res = new ArrayList<>();
		gen_permutation(nums, 0, res);
		return result_list;
	}

	public static void main(String[] args) {
//		String string = "123";
//		string = string.substring(0, 1);
//		System.out.println(string);

		 int[] arr = new int[] { 1, 2, 3 };
		 List<ArrayList<Integer>> rse = my_permutation(new int[] { 1, 2});
		 System.out.println(rse);

	}

}
