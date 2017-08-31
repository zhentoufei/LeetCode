package easy;
import java.util.HashMap;

public class MaxLen {

	public static int maxLength(int[] arr, int k) {
		if (arr == null || arr.length == 0) {
			return 0;
		}
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		map.put(0, -1); // important
		int len = 0;
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
			if (map.containsKey(sum - k)) {
				len = Math.max(i - map.get(sum - k), len); //map中的get是获得元素
			}
			if (!map.containsKey(sum)) {
				map.put(sum, i);
			}
		}
		return len;
	}

	public static int[] generateArray(int size) {
		int[] result = new int[size];
		for (int i = 0; i != size; i++) {
			result[i] = (int) (Math.random() * 11) - 5;
		}
		return result;
	}


	public static void main(String[] args) {
//		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
//		map.put(1, 2);
//		System.out.println(map.get(2));
		int[] arr = { 5, 3, 1, 1, 1, 1, 1, 2 };
		int sum = 0;
		int k = 5;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		int n = sum / k;
		int max = 0;
		for (int i = 1; i <= n; i++) {
			int l = maxLength(arr, k * i);
			if (max < l) {
				max = l;
			}
		}
		System.out.println(max);
		System.out.println(max);

	}

}
