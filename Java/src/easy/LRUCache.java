package easy;

import java.util.HashMap;

import com.sun.org.apache.bcel.internal.generic.INEG;

import javafx.geometry.Pos;

class DoubleLinkedListNode {

	public int val;
	public int key;
	public DoubleLinkedListNode pre;
	public DoubleLinkedListNode next;

	public DoubleLinkedListNode(int key, int value) {
		val = value;
		this.key = key;
	}
}

public class LRUCache {

	private HashMap<Integer, DoubleLinkedListNode> map = new HashMap<>();
	private DoubleLinkedListNode head;
	private DoubleLinkedListNode end;
	private int capacity;
	private int len;

	public LRUCache(int capacity) {
		this.capacity = capacity;
		len = 0;
	}

	public int get(int key) {
		if (map.containsKey(key)) {
			DoubleLinkedListNode latest = map.get(key);

		}
		return 0;
	}

	public void removeNode(DoubleLinkedListNode node) {
		DoubleLinkedListNode cur = node;
		DoubleLinkedListNode pre = cur.pre;
		DoubleLinkedListNode pst = cur.next;

		if (pre != null)
			pre.next = pst;
		else
			head = pst;

		if (pst != null)
			pst.pre = pre;
		else
			end = pre;
	}

	public void setHead(DoubleLinkedListNode node) {
		node.next = head;
		node.pre = null;
		if (head != null)
			head.pre = node;

		head = node;
		if (end == null)
			end = node;

	}

	public void set(int key, int value) {
		if (map.containsKey(key)) {
			DoubleLinkedListNode old_node = map.get(key);
			old_node.val = value;
			removeNode(old_node);
			setHead(old_node);
		}
	}

	public void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
