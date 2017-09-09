package easy;

import java.util.ArrayList;
import java.util.List;

public class Triangle {

	private static List<Integer> result = new ArrayList<>();
	private static List<List<Integer>> index_path = new ArrayList<>();
	private static List<Integer> last_sum = new ArrayList<>();

	public static void get_path(List<List<Integer>> triangle, int index, List<Integer> previous_sum) {
		if (index == triangle.size()) {
			last_sum = previous_sum;
			return;
		}

		List<Integer> present_sum = new ArrayList<>();
		List<Integer> present_index_path = new ArrayList<>();// 记录上次的位置
		for (int i = 0; i < triangle.get(index).size(); i++) {

			if (i == triangle.get(index).size() - 1) {
				present_sum.add(previous_sum.get(i - 1));
				present_index_path.add(triangle.get(index).size() - 1);

			} else if (i == 0) {
				present_sum.add(previous_sum.get(i));
				present_index_path.add(0);
			} else {
				List<Integer> present_line = triangle.get(index);// 获得当前行
				if (previous_sum.get(i - 1) < previous_sum.get(i)) {
					present_index_path.add(i - 1);
					present_sum.add(previous_sum.get(i - 1) + present_line.get(i));
				} else {
					present_index_path.add(i);
					present_sum.add(previous_sum.get(i) + present_line.get(i));
				}
			}
		}
		index_path.add(present_index_path);
		get_path(triangle, index + 1, present_sum);

	}

	public static List<Integer> get_result() {
		List<Integer> res = new ArrayList<>();
		int min_index = 0;
		int min = last_sum.get(0);
		for (int i = 1; i < last_sum.size(); i++) {
			if (min > last_sum.get(i)) {
				min = last_sum.get(i);
				min_index = i;
			}
		}
		result.add(min_index);
		for (int j = index_path.size() - 1; j >= 0; j--) {
			result.add(index_path.get(j).get(result.get(result.size() - 1)));
		}
		return res;
	}

	public static List<Integer> triangle(List<List<Integer>> triangle) {
		int index_len = triangle.size();

		if (index_len == 1) {
			result.add(1);
			return result;
		}
		List<Integer> tmp_sum = new ArrayList<>();
		tmp_sum.add(triangle.get(0).get(0));
		get_path(triangle, 1, tmp_sum);
		return result;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<List<Integer>> arr = new ArrayList<>();
		List<Integer> a1 = new ArrayList<>();
		a1.add(2);
		arr.add(a1);
		List<Integer> a2 = new ArrayList<>();
		a2.add(3);
		a2.add(4);
		arr.add(a2);
		List<Integer> a3 = new ArrayList<>();
		a3.add(6);
		a3.add(5);
		a3.add(7);
		arr.add(a3);
		List<Integer> a4 = new ArrayList<>();
		a3.add(4);
		a3.add(1);
		a3.add(8);
		a3.add(3);
		arr.add(a4);
		triangle(arr);
		System.out.println(get_result());

	}

}
