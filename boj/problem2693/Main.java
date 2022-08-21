package problem2693;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int A_LENGTH = 10;

    public static String solve(int[][] arrs) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < arrs.length; i++) {
            int[] arrA = arrs[i];
            Arrays.sort(arrA);
            if (i == 0)
                sb.append(Integer.toString(arrA[A_LENGTH - 3]));
            else
                sb.append("\n").append(Integer.toString(arrA[A_LENGTH - 3]));
        }

        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        int[][] arrs = new int[T][A_LENGTH];
        for (int i = 0; i < T; i++) {
            int[] A = new int[A_LENGTH];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < A.length; j++) {
                A[j] = Integer.parseInt(st.nextToken());
            }
            arrs[i] = A;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(arrs));
        bw.flush();
    }
}
