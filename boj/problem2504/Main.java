package problem2504;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static String solve(String brackets) {
        int answer = 0;
        Stack<String> st = new Stack<>();

        String s1;
        int temp = 1;
        for (int i = 0; i < brackets.length(); i++) {
            s1 = brackets.substring(i, i + 1);

            if (s1.equals("(")) {
                temp *= 2;
                st.push(s1);
            } else if (s1.equals("[")) {
                temp *= 3;
                st.push(s1);
            } else if (s1.equals(")")) {
                if (st.isEmpty() || !st.peek().equals("(")) {
                    answer = 0;
                    break;
                } else if (brackets.substring(i - 1, i).equals("(")) {
                    answer += temp;
                    temp /= 2;
                    st.pop();
                } else if (!brackets.substring(i - 1, i).equals("(")) {
                    temp /= 2;
                    st.pop();
                }
            } else if (s1.equals("]")) {
                if (st.isEmpty() || !st.peek().equals("[")) {
                    answer = 0;
                    break;
                } else if (brackets.substring(i - 1, i).equals("[")) {
                    answer += temp;
                    temp /= 3;
                    st.pop();
                } else if (!brackets.substring(i - 1, i).equals("[")) {
                    temp /= 3;
                    st.pop();
                }
            }
        }

        if (!st.isEmpty())
            return Integer.toString(0);

        return Integer.toString(answer);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String brackets = st.nextToken();

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(brackets));
        bw.flush();
    }
}
