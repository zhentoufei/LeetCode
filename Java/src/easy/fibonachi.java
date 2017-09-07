package easy;

public class fibonachi {

	public static int[] memo;

	public static int fib(int n) {
		if (n == 0)
			return 1;
		if (n == 1)
			return 1;
		if (memo[n] == -1)
			memo[n] = fib(n - 1) + fib(n - 2);
		return memo[n];
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 4;
		memo = new int[n + 1];
		for (int i = 0; i < memo.length; i++) {
			memo[i] = -1;
		}
		System.out.println(fib(n));
	}

}
