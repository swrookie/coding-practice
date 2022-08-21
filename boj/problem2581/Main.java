package problem2581;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int M, int N) {
        int answer = -1;
        int[] arr = new int[N + 1];
        arr[1] = -1;
        int sum = 0;
        int minNum = Integer.MAX_VALUE;

        for (int i = M; i < N + 1; i++) {
            if (arr[i] == -1)
                continue;

            int divisible = 0;
            for (int j = 1; j < i / 2 + 1; j++) {
                if (i % j == 0) {
                    divisible = j;
                }
            }

            if (divisible == 1) {
                sum += i;
                minNum = Math.min(i, minNum);
                for (int j = i + i; j < N + 1; j += i) {
                    arr[j] = -1;
                }
            }
        }

        if (sum == 0 && minNum == Integer.MAX_VALUE)
            return Integer.toString(answer);

        return sum + "\n" + minNum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(M, N));
        bw.flush();
    }
}
