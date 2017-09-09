package easy;

import java.util.ArrayList;
import java.util.List;


public class NQueen {

	private static List<String> res = new ArrayList<>();
	private static Boolean[] col;
	private static Boolean[] diag_left;
	private static Boolean[] diag_right;

	// 这里要通过index 的索引来指导n的结束
	private static void put_queen(int n, int index, String res_tmp) {

		if (index == n) {
			res.add(res_tmp);
			System.out.println("--------------");
			return;
		}
		for (int i = 0; i < n; i++) {
			if (!col[i] && !diag_left[index + i] && !diag_right[index - i + n - 1]) {
				res_tmp += i;
				col[i] = true;
				diag_left[index + i] = true;
				diag_right[index - i + n - 1] = true;
				System.out.println(index + "----");
				put_queen(n, index + 1, res_tmp);
				col[i] = false;
				diag_left[index + i] = false;
				diag_right[index - i + n - 1] = false;
				res_tmp = res_tmp.substring(0, res_tmp.length() - 1);

			}
		}
		return;
	}

	public static List<String> NQueens(int n) {
		col = new Boolean[n];
		diag_left = new Boolean[2 * n - 1];
		diag_right = new Boolean[2 * n - 1];
		for (int i = 0; i < n; i++) {
			col[i] = false;
		}
		for (int i = 0; i < 2 * n - 1; i++) {
			diag_left[i] = false;
			diag_right[i] = false;
		}
		put_queen(n, 0, "");

		return res;

	}

	public static void main(String[] args) {
		List<String> reStrings = NQueens(4);
		System.out.println(reStrings);
		// String s = "123";
		// System.out.println(s.substring(0,s.length()-1));

	}

}
