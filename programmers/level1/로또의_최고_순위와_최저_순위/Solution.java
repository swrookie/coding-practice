// package programmers.level1.로또의_최고_순위와_최저_순위;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];

        int match = 0;
        int zeros = 0;

        for (int lotto : lottos) {
            if (lotto == 0)
                zeros++;
        }

        for (int win_num : win_nums) {
            if (IntStream.of(lottos).anyMatch(x -> x == win_num)) {
                match++;
            }
        }

        answer[0] = 7 - (match + zeros) < 7 ? 7 - (match + zeros) : 6;
        answer[1] = 7 - match < 7 ? 7 - match : 6;

        return answer;
    }

    public static void main(String[] args) {
        int[] lottos = { 44, 1, 0, 0, 31, 25 };
        int[] win_nums = { 31, 10, 45, 1, 6, 19 };

        System.out.println(Arrays.toString(new Solution().solution(lottos, win_nums)));
    }
}