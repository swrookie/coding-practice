package problem2460;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {
    public static String solve(int[][] arr) {
        int answer = 0;
        int currCnt = 0;
        int maxCnt = -1;

        for (int i = 0; i < arr.length; i++) {
            currCnt = currCnt - arr[i][0] + arr[i][1];
            maxCnt = Math.max(currCnt, maxCnt);
        }

        answer = maxCnt;

        return Integer.toString(answer);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] arr = new int[10][2];

        for (int i = 0; i < arr.length; i++) {
            st = new StringTokenizer(br.readLine());
            int offboard = Integer.parseInt(st.nextToken());
            int onboard = Integer.parseInt(st.nextToken());
            int[] nums = {offboard, onboard};
            arr[i] = nums;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(arr));
        bw.flush();
    }
}
