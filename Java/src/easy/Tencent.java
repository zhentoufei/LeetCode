package easy;

import java.util.Scanner;

public class Tencent {

	/*
	 * ����һ����Ѷǰ�˵�һ�������
	 * 
	 * СQ������ ʱ�����ƣ�ÿ��case��2s�� �ռ����ƣ�128M
	 * 
	 * СQ��ѧϰѪ�������㷨֮�����һ�������Լ�����һ�������㷨��СQϣ���������n����ͬ��������Ϊ���� СQ�����������㷨��ÿ���������ֲ����� 1.
	 * ����ǰ�����е�ǰn-1��������Ϊ���� 2. ����ǰ�����еĺ�n-1��������Ϊ����
	 * СQ������һ��ʹ���������ֲ�����СQ�����뿼����������Ҫ��������������������������
	 * 
	 * ���룺 ����������У���һ�а���һ��������n(3<=n<=10^5),��ʾ���ֵĸ���
	 * �ڶ��а���n��������a[i](i<=a[i]<=10^9),����Ҫ��������֣���֤���ָ�����ͬ
	 * 
	 * 
	 * ����� ���һ������������ʾ������Ҫ�Ĳ�������
	 * 
	 * �������룺 6 4 3 1 6 2 5 �����2
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
