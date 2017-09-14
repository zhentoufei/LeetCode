package easy;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class TurnOffLight {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int len = sc.nextInt();
		int[] arr = new int[len];
		for (int i = 0; i < len; i++) {
			arr[i] = sc.nextInt();
		}
		List<Integer> int_arr = new ArrayList<>();
		for (int i = 0; i < len; i++) {
			if(arr[i]%7 == 0)
				int_arr.add(arr[i]);
		}
		Set<Integer> arr_set = new HashSet<>();
		for (int i = 0; i < int_arr.size(); i++) {
			arr_set.add(int_arr.get(i));
		}
		System.out.print(arr_set.size()*(arr_set.size()-1));

	}

}