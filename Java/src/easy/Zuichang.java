package easy;

import java.util.ArrayList;
import java.util.Iterator;

public class Zuichang {

	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<Integer>();// 新建一个ArrayList集合
		for (int i = 1; i < 101; i++) {// 循环100，把100个元素加到集合中
			list.add(i);
		}

		ArrayList<Integer> newList1 = new ArrayList<Integer>();// 新建一个集合，用于保存每次退出的那个人。

		newList1 = getIndex();// 调用getIndex方法，给集合添加元素。
		list.removeAll(newList1);// 100人的集合，减去退出人的集合，就得到剩下的人13个人

		System.out.println("最后剩下的人数为：" + list.size());// 还剩下13个人。
		Iterator it = list.iterator();// 获取迭代器
		while (it.hasNext()) {// 遍历输出所剩下的人。
			System.out.println("剩下的人是100人中的第：" + it.next() + "个");
		}

	}

	// 定义一个方法，获取每次退出的那个人的索引
	private static ArrayList getIndex() {
		ArrayList<Integer> newList2 = new ArrayList<Integer>();// 创建一个新集合，用于保存退出的人
		int count = 0;// 定义一个变量，记录数数值。

		for (int i = 1; i < 101; i++) {
			count++;
			while (newList2.contains(i)) {// 判断集合是否已经有i
				i++;// 如果集合已经有这个元素，就往后加一个，直到集合中没有那个元素为止。
				if (i == 101) {// 如果数到了100个，
					i = 1;// 返回来再重头数。
				}
			}
			if ((count % 14 == 0)) {// 如果数到14，就将i加到集合中。
				newList2.add(i);
				count = 0;// 计数清零，重新计数。
			}
			if (i == 100) {// 如果数到100
				i = 1;// 跳回来重新数。
			}
			if (newList2.size() > (100 - 14)) {// 当集合里面添加的人数达到87人时，退出循环。
				break;
			}
		}
		return newList2;
	}
}
