package problem10870;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int n) {
        int[] fibs = new int[n + 2];
        fibs[0] = 0;
        fibs[1] = 1;

        if (n == 0 || n == 1)
            return Integer.toString(fibs[n]);

        for (int i = 2; i < n + 1; i++) {
            fibs[i] = fibs[i - 1] + fibs[i - 2];
        }

        return Integer.toString(fibs[n]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(n));
        bw.flush();
    }
}
