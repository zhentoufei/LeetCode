package easy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class ×Ö·û´®Ñ¹Ëõ {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		String input_raw = scanner.nextLine();
		String[] input_split = input_raw.split(" ");
		int len = input_split.length;
		List<Integer> input_list = new ArrayList<>();
		for (int i = 0; i < len; i++) {
			input_list.add(Integer.parseInt(input_split[i]));
		}
		Collections.sort(input_list);
		input_list.add(-1);
		String reString = "";
		Integer counter = 1;
		for (int i = 0; i < len; i++) {
			if (input_list.get(i) == input_list.get(i + 1)) {
				counter++;
			} else if (input_list.get(i) != input_list.get(i + 1)) {
				reString = reString + input_list.get(i) + " " + counter + " ";
				counter = 1;
			}
		}
		
		System.out.print(reString.trim());
		
	}

}
