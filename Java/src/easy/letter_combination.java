package easy;

import java.util.ArrayList;
import java.util.List;

public class letter_combination {

	private static List<String> results_list = new ArrayList<>();
	private static String[] digits_map = { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

	// digits输入的数字字符串
	// index当前正在处理的数字位数
	// 上一论处理的结果
	private static void find_combinations(String digits, int index, String res) {

		// 终止条件
		if (index == digits.length()) {
			results_list.add(res);
			return;
		}

		char present_num = digits.charAt(index);
		if (present_num >= '0' && present_num <= '9' && present_num != '1') {
			// TODO something
		}
		String present_letters = digits_map[present_num - '0'];
		for (int i = 0; i < present_letters.length(); i++) {
			find_combinations(digits, index + 1, res + present_letters.charAt(i));
		}
		return;
	}

	public static List<String> letter_combinations(String digits) {
		
		results_list.clear();
		find_combinations(digits, 0, "");
		
		return results_list;
	}

	public static void main(String[] args) {
		List<String> reStrings = letter_combinations("234");
		for (String string : reStrings) {
			System.out.println(string);
		}

	}

}
