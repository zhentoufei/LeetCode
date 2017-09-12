package easy;

import java.util.Scanner;

public class Tencent {

	/*
	 * 更新一波腾讯前端的一个编程题
	 * 
	 * 小Q的排序 时间限制（每个case）2s； 空间限制：128M
	 * 
	 * 小Q在学习血多排序算法之后灵机一动决定自己发明一种排序算法，小Q希望嗯你过奖n个不同的数排序为升序 小Q发明的排序算法在每轮允许两种操作： 1.
	 * 将当前序列中的前n-1个数排序为升序 2. 将当前序列中的后n-1个数排序为升序
	 * 小Q可以人一次使用上述两种操作，小Q现在想考考你最少需要几次上述操作可以让序列有序
	 * 
	 * 输入： 输入包括两行，第一行包括一个正整数n(3<=n<=10^5),表示数字的个数
	 * 第二行包括n个正整数a[i](i<=a[i]<=10^9),即需要排序的数字，保证数字各不相同
	 * 
	 * 
	 * 输出： 输出一个正整数，表示最少需要的操作次数
	 * 
	 * 样例输入： 6 4 3 1 6 2 5 输出：2
	 *
	 * * *?
	 */

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int len = Integer.parseInt(scan.nextLine());
		String raw_input = scan.nextLine();
		String[] _arr = raw_input.toString().split(" ");
		scan.close();
		int[] arr = new int[len];
		for (int i = 0; i < len; i++) {
			arr[i] = Integer.parseInt(_arr[i]);
		}

		int first = arr[0];
		int last = arr[len - 1];
		int max = first;
		int min = first;
		for (int i = 0; i < len - 1; i++) {
			if (min > arr[i])
				min = arr[i];
			if (max < arr[i])
				max = arr[i];
		}

		if (first < last) {
			if (last > max)
				System.out.println(1);
			else
				System.out.println(2);
		} else {
			if (first > max)
				System.out.println(3);
			else
				System.out.println(2);
		}

	}

}
