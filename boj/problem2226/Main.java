package problem2226;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int N) {
        BigInteger answer = BigInteger.valueOf(0);
        BigInteger[] oneStartArr = {BigInteger.valueOf(0), BigInteger.valueOf(1)};
        BigInteger[] zeroStartArr = {BigInteger.valueOf(0), BigInteger.valueOf(1)};

        if (N == 1 || N == 2)
            return oneStartArr[N - 1].toString();

        for (int i = 2; i < N; i++) {
            BigInteger prevOneStartZeroCnt = oneStartArr[1];
            BigInteger prevZeroStartZeroCnt = zeroStartArr[1];
            if ((i - 1) % 2 != 0) {
                oneStartArr[1] = prevOneStartZeroCnt.add(prevZeroStartZeroCnt)
                        .subtract(BigInteger.valueOf(1));
                oneStartArr[0] = prevOneStartZeroCnt;
                zeroStartArr[1] = prevOneStartZeroCnt.add(prevZeroStartZeroCnt);
                zeroStartArr[0] = prevZeroStartZeroCnt;
            } else {
                oneStartArr[1] = prevOneStartZeroCnt.add(prevZeroStartZeroCnt);
                oneStartArr[0] = prevOneStartZeroCnt;
                zeroStartArr[1] = prevOneStartZeroCnt.add(prevZeroStartZeroCnt);
                zeroStartArr[0] = prevZeroStartZeroCnt;
            }
        }

        answer = oneStartArr[1];

        return answer.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(N));
        bw.flush();
    }
}
