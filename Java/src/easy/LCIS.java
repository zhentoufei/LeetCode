package easy;
import java.util.Scanner;

public class LCIS {

	
	public int longestCommonIncreaseSubsequence(String A, String B) {
        if(A == null || B == null){
            return 0;
        }
        int m = A.length();
        int n = B.length();
        int [][] dp = new int[m+1][n+1];
        for(int i = 1; i<=m; i++){
            for(int j = 1; j<=n; j++){
            	
                if(A.charAt(i-1) == B.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1]+1;
                    
                }else{
                    dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]);
                }
            }
        }
        return dp[m][n];
    }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);

		String[] first_line = scan.nextLine().split(" ");
		
		Integer given_series_len = Integer.parseInt(first_line[0]);
		Integer target_series_len = Integer.parseInt(first_line[1]);
		
		Integer lcis_len = Integer.parseInt(scan.nextLine());

		String[] third_line = scan.nextLine().split(" ");
		Integer left = Integer.parseInt(third_line[0]);
		Integer right = Integer.parseInt(third_line[1]);

		String[] given_series_of_n = scan.nextLine().split(" ");
		int[] given_series = new int[given_series_len];
		int i = 0;
		for (String serie : given_series_of_n) {
			given_series[i++] = Integer.parseInt(serie);
		}
		scan.close();

		int[][] dp;
		int[] gen_series = new int[target_series_len];
		
		

	}

}
