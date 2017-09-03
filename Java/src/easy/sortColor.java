package easy;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class sortColor {

	
	//private========================================
	private static String[] stringMap = { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
	private static List<String> res = new ArrayList<>();

	
	//public========================================
	public static void find_combination(String digits, int index, String s) {
		if (index == digits.length()) {
			res.add(s);
			return;
		}

		char c = digits.charAt(index);
		String letters = stringMap[c - '0'];
		for (int i = 0; i < letters.length(); i++) {
			find_combination(digits, index + 1, s + letters.charAt(i));
		}
		return;

	}
	
	public static void main(String[] args) {
//		List<String> reStrings = find_combination("345", 0, "");
		// TODO Auto-generated method stub
		// Scanner scan = new Scanner(System.in);
		// String target = scan.nextLine();
		// String[] target_Str_list = target.split(" ");


	}

}
