package easy;

import java.util.ArrayList;
import java.util.Iterator;

public class Zuichang {

	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<Integer>();// �½�һ��ArrayList����
		for (int i = 1; i < 101; i++) {// ѭ��100����100��Ԫ�ؼӵ�������
			list.add(i);
		}

		ArrayList<Integer> newList1 = new ArrayList<Integer>();// �½�һ�����ϣ����ڱ���ÿ���˳����Ǹ��ˡ�

		newList1 = getIndex();// ����getIndex���������������Ԫ�ء�
		list.removeAll(newList1);// 100�˵ļ��ϣ���ȥ�˳��˵ļ��ϣ��͵õ�ʣ�µ���13����

		System.out.println("���ʣ�µ�����Ϊ��" + list.size());// ��ʣ��13���ˡ�
		Iterator it = list.iterator();// ��ȡ������
		while (it.hasNext()) {// ���������ʣ�µ��ˡ�
			System.out.println("ʣ�µ�����100���еĵڣ�" + it.next() + "��");
		}

	}

	// ����һ����������ȡÿ���˳����Ǹ��˵�����
	private static ArrayList getIndex() {
		ArrayList<Integer> newList2 = new ArrayList<Integer>();// ����һ���¼��ϣ����ڱ����˳�����
		int count = 0;// ����һ����������¼����ֵ��

		for (int i = 1; i < 101; i++) {
			count++;
			while (newList2.contains(i)) {// �жϼ����Ƿ��Ѿ���i
				i++;// ��������Ѿ������Ԫ�أ��������һ����ֱ��������û���Ǹ�Ԫ��Ϊֹ��
				if (i == 101) {// ���������100����
					i = 1;// ����������ͷ����
				}
			}
			if ((count % 14 == 0)) {// �������14���ͽ�i�ӵ������С�
				newList2.add(i);
				count = 0;// �������㣬���¼�����
			}
			if (i == 100) {// �������100
				i = 1;// ��������������
			}
			if (newList2.size() > (100 - 14)) {// ������������ӵ������ﵽ87��ʱ���˳�ѭ����
				break;
			}
		}
		return newList2;
	}
}
