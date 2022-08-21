package problem1978;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int[] arr) {
        int answer = 0;
        Arrays.sort(arr);
        int maxNum = arr[arr.length - 1];
        int[] primes = new int[maxNum + 1];
        primes[1] = -1;

        int cnt = 0;
        for (int num : arr) {
            if (primes[num] == -1)
                continue;

            int divisible = 0;
            for (int j = 1; j < num / 2 + 1; j++) {
                if (num % j == 0)
                    divisible = j;
            }

            if (divisible == 1) {
                cnt++;
                for (int j = num; j <= maxNum; j += num) {
                    primes[j] = -1;
                }
            }
        }

        answer = cnt;

        return Integer.toString(answer);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(arr));
        bw.flush();
    }
}
