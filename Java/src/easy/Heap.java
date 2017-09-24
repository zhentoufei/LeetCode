package easy;

public class Heap<Item extends Comparable> {

	protected Item[] data;
	protected int count;
	protected int capacity;

	public Heap(int capacity) {
		data = (Item[]) new Comparable[capacity + 1];
		count = 0;
		this.capacity = capacity;
	}

	public Heap(Item[] arr) {
		int n = arr.length;
		data = (Item[]) new Comparable[n + 1];
		capacity = n;
		for (int i = 0; i < n; i++)
			data[i + 1] = arr[i];
		count = n;

		for (int i = count / 2; i >= 1; i--)
			shiftDown(i);
	}

	public int size() {
		return count;
	}

	public boolean isEmpty() {
		return count == 0;
	}

	private void insert(Item item) {
		assert count + 1 <= capacity;

		count++;
		data[count] = item;
		shift_up(count);
	}

	public Item extraMax() {
		assert count > 0;
		Item res = data[1];

		swap(1, count);
		count--;
		shiftDown(1);

		return res;
	}

	public Item getMax() {
		assert count > 0;
		return data[1];
	}

	// ********************
	// * 最大堆核心辅助函数
	// ********************
	private void shift_up(int k) {
		while (k > 1 && data[k / 2].compareTo(data[k]) < 0) {
			swap(k, k / 2);
			k /= 2;
		}

	}

	private void shiftDown(int k) {
		while (k * 2 <= count) {
			int j = 2 * k;
			if (j + 1 <= count && data[j + 1].compareTo(data[j]) > 0)
				j++;
			if (data[k].compareTo(data[j]) > 0)
				break;
			swap(k, j);
			k = j;
		}
	}

	private void swap(int i, int j) {
		Item tItem = data[i];
		data[i] = data[j];
		data[j] = tItem;
	}

	// 此时我们是将数据一个一个的插入到堆中的
	// 将n个元素逐个插入到一个空堆中，算法复杂度是O(nlogn)
	public static void heapSort1(Comparable[] arr) {
		int n = arr.length;
		Heap<Comparable> max_heap = new Heap<>(n);
		for (int i = 0; i < n; i++) {
			max_heap.insert(arr[i]);
		}
		for (int i = n - 1; i >= 0; i--)
			arr[i] = max_heap.extraMax();
	}

	// heapify的过程，算法复杂度为O(n)
	public static void headSort2(Comparable[] arr) {
		int n = arr.length;
		Heap<Comparable> max_heap = new Heap<>(n);
		for (int i = n - 1; i >= 0; i--) {
			arr[i] = max_heap.extraMax();
		}
	}

	public static void main(String[] args) {
		// Heap<Integer> max_heap = new Heap<>(100);
		// int N = 100;
		// int M = 100;
		// for (int i = 0; i < N; i++)
		// max_heap.insert(new Integer((int) (Math.random() * M)));
		// Integer[] arr = new Integer[N];
		//
		// Integer[] arr = { 1, 2, 3, 8, 7, 6, 5, 4 };
		// Heap<Integer> max_heap = new Heap<>(arr);
		// for (int i = 0; i < 8; i++) {
		// arr[i] = max_heap.extraMax();
		// System.out.println(arr[i]);
		// }
		Comparable[] arr = {'1','2','3','2','2'};
		int[] int_arr = (int[])arr;
		System.out.println();
		
		
	}

}
