package problem1292;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_NUM = 1000;

    public static String solve(int A, int B) {
        int answer = 0;
        int[] arr = new int[MAX_NUM + 1];

        int num = 1;
        int counter = 0;
        for (int i = 1; i < MAX_NUM; i++) {
            arr[i] = num;
            counter++;
            if (num == counter) {
                num++;
                counter = 0;
            }
        }

        int sum = 0;
        for (int i = A; i <= B; i++) {
            sum += arr[i];
        }

        answer = sum;
        return Integer.toString(answer);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(A, B));
        bw.flush();
    }
}
