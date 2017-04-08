package com.easy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/*
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
 Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 * */
public class TwoSum 
{
	public static void main(String[] args) {
		int[] a = new int[]{1,3,5,6,2,4};
		int target = 6;
		System.out.print("����ı��������Ķ�����");
		int[] res = twoSum2(a,target);
		for (int ele : res) {
			System.out.print(ele);
		}
	}
	public static int[] twoSum2(int[] nums, int target) {  
        int index1,index2;  
        int[] index=new int[]{0,1};  
        Set<Integer> nset= new HashSet<>();
          
        for(int i = 0; i< nums.length; i++)  
        {  
           if(nset.add(target-nums[i])) //����Ƿ���nums[i]��Ե�Ԫ�ش��ڣ�������ӳɹ�   
           {  
               nset.remove(target-nums[i]); //��Ӹ�Ԫ��ֻ��Ϊ���ж��Ƿ���ڣ�������Ӧ����ӵ�������ɾ��  
               nset.add(nums[i]);  
           }else  
           {  
               index[1] = i+1;  
               for(int j = 0; j< i; j++)  
               {  
                   if(target==(nums[i]+nums[j]))  
                   {  
                       index[0] = j+1;  
                       return index;  
                   }  
               }  
               return index;  
           }  
             
        }  
        return index;  
    }  
	public int[] twoSum3(int[] nums, int target) {    
        int[] index=new int[]{0,1};  
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();  
          
        for(int i = 0; i<nums.length; i++)  
        {  
            if(hm.containsKey(target - nums[i]))  
            {  
                index[1] = i+1;  
                index[0] = hm.get(target-nums[i])+1;     
                return index;     
            }else  
            {  
                 hm.put(nums[i],i);  
            }  
        }  
        return index;    
    }  
	public static int[] twoSum(int[] nums, int target)
	{
		Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(target-nums[i])){
                int[] index={map.get(target-nums[i]),i};
                return index;
            }
            map.put(nums[i],i+1);
        }
        return null;
    }
}
