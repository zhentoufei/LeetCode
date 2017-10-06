package easy;

import java.util.Arrays;
import java.util.Scanner;


public class yuehui {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String str1 = scanner.nextLine();
		String str2 = scanner.nextLine();
		String arr1 = str1.split("-").toString();
		String arr2 = str2.split("-").toString();
		System.out.println(arr2);
		char[] ca1 = arr1.toCharArray();
		for (char c : ca1) {
			System.out.println(c);
		}
		
		
		

	}

}
//var a = readline();
//var b = readline();
//var ArrA = a.split('-').reverse();
//var ArrB = b.split('-').reverse();
//
//var len = Math.max(ArrA.length,ArrB.length);
//var sum = 0;
//var result = '';
//for (var i=0; i<len; i++){
//    if (ArrA[i] == ArrB[i]){
//        sum++;
//        result = ArrA[i];
//    }
//}
//if(sum  == 0){
//    console.log(0 + ' ' + 0);
//}else {
//    	sum--;
//    	console.log(result + ' ' + sum);
//	}

