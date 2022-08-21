package problem2309;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int N = 9;
    private static final int REAL_N = 7;
    private static ArrayList<int[]> answers = new ArrayList<>();

    public static void backtrack(int depth, boolean[] visited, int[] arr, int[] combs) {
        if (depth == REAL_N) {
            int[] temp = new int[N];
            int sum = 0;
            for (int i = 0; i < combs.length; i++) {
                sum += combs[i];
                temp[i] = combs[i];

            }

            if (sum == 100)
                answers.add(temp);

            return;
        }

        for (int i = depth; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                combs[i] = arr[i];
                backtrack(depth + 1, visited, arr, combs);
                combs[i] = 0;
                visited[i] = false;
            }
        }
    }

    public static String solve(int[] arr) {
        boolean[] visited = new boolean[N];
        int[] combs = new int[N];

        backtrack(0, visited, arr, combs);

        int[] answer = answers.get(0);
        Arrays.sort(answer);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < answer.length; i++) {
            if (i == 0 && answer[i] != 0)
                sb.append(Integer.toString(answer[i]));
            else if (answer[i] != 0)
                sb.append("\n").append(Integer.toString(answer[i]));
        }

        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(solve(arr));
        bw.flush();
    }
}
