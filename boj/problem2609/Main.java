package problem2609;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static String solve(int num1, int num2) {
        int maxNum = Math.max(num1, num2);
        int minNum = Math.min(num1, num2);
        int gcd = 0;
        int lcm = 0;

        for (int i = minNum; i > 0; i--) {
            if (num1 % i == 0 && num2 % i == 0) {
                gcd = i;
                break;
            }
        }

        int increment = maxNum;
        while (true) {
            if (maxNum % num1 == 0 && maxNum % num2 == 0) {
                lcm = maxNum;
                break;
            }
            maxNum += increment;
        }

        return Integer.toString(gcd) + "\n" + Integer.toString(lcm);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num1 = Integer.parseInt(st.nextToken());
        int num2 = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(num1, num2));
        bw.flush();
    }
}
