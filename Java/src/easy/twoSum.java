package easy;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class twoSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		String str=scan.nextLine();
		int[] nums=transInt(str);
	}
	
	public static int[] transInt(String numberString){
		char[] digitNumberArray = numberString.toCharArray();
		int[] digitArry = new int[numberString.toCharArray().length];
		for (int i = 0; i < digitNumberArray.length; i++) {
		    digitArry[i] = digitNumberArray[i]-'0';
		}
		return digitArry;
	}
	public static int[] twoSum1(int[] nums, int target) {
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
