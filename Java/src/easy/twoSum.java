package easy;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class twoSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		String target=scan.nextLine();
		String str=scan.nextLine();
		scan.close();
		int[] nums=transInt(str);
		for (int k : nums) {
			System.out.print(k);
		}
		//int[] res=twoSumFunction(nums, Integer.parseInt(target));
		int[] res=twoSumFunction(new int[]{1,2,3,4},7);
		for (int i : res) {
			System.out.print(i);
		}
	}
	
	public static int[] transInt(String numberString){
		char[] digitNumberArray = numberString.toCharArray();
		int[] digitArry = new int[numberString.toCharArray().length];
		for (int i = 0; i < digitNumberArray.length; i++) {
//		    digitArry[i] = Integer.parseInt(digitNumberArray[i]);
		}
		return digitArry;
	}
	public static int[] twoSumFunction(int[] nums, int target) {
		Map<Integer, Integer> map=new HashMap<>();
		for(int i =0;i<nums.length;i++){
			if(map.containsKey(target-nums[i])){
				int[] index={map.get(target-nums[i]),i};
				return index;
			}
			map.put(nums[i], i);
		}
		return null;
	}
}
