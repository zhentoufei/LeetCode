package easy;

import java.util.ArrayList;
import java.util.List;

public class NumberOfGame {

	public static ArrayList<Integer> list_100 = new ArrayList<>();
	public static List<Integer> list_index = new ArrayList<>();
	public static Boolean flag = true;

	public static void main(String[] args) {
		for (int i = 0; i < 100; i++) {
			list_100.add(i+1);
		}

		NumberOffGame(4, list_100);
		for (Integer ele : list_100) {
			System.out.println(ele);
		}

	}

	private static void NumberOffGame(int m, ArrayList<Integer> res) {
		int count = 0;
		int present_index = 0;
		while (flag) {
			if (m > list_100.size()) {
				break;
			}

			if (count % m == 0) {
				list_100.remove(present_index);
				present_index--;
				count = 0;
			}
			count++;
			present_index++;
			if (present_index >= list_100.size()) {
				present_index = 0;
			}

		}
	}

}
