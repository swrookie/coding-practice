package problem2501;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int N, int K) {
        int answer = 0;
        int k = 0;

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                k++;

                if (k == K)
                    return Integer.toString(i);
            }
        }

        return Integer.toString(answer);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(N, K));
        bw.flush();
    }
}
