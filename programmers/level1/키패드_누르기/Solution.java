import java.util.*;

public class Solution {
    // 유클리드 거리 구하기 (피타고라스 공식이랑 비슷한 것 같다)
    public double euclideanDistance(int[] coordOne, int[] coordTwo) {
        return Math.sqrt(Math.abs(coordOne[0] - coordTwo[0]) + Math.abs(coordOne[1] - coordTwo[1]));
    }

    // 맨해튼 거리 (이 문제에선 이 공식이 맞는 것 같다)
    public int manhattanDistance(int[] coordOne, int[] coordTwo) {
        return Math.abs(coordOne[0] - coordTwo[0]) + Math.abs(coordOne[1] - coordTwo[1]);
    }

    public String solution(int[] numbers, String hand) {
        StringBuilder rightThumbLoc = new StringBuilder("*");
        StringBuilder leftThumbLoc = new StringBuilder("#");

        Map<String, int[]> keyPad = new HashMap<>();

        keyPad.put("1", new int[] { 0, 0 });
        keyPad.put("2", new int[] { 0, 1 });
        keyPad.put("3", new int[] { 0, 2 });
        keyPad.put("4", new int[] { 1, 0 });
        keyPad.put("5", new int[] { 1, 1 });
        keyPad.put("6", new int[] { 1, 2 });
        keyPad.put("7", new int[] { 2, 0 });
        keyPad.put("8", new int[] { 2, 1 });
        keyPad.put("9", new int[] { 2, 2 });
        keyPad.put("*", new int[] { 3, 0 });
        keyPad.put("0", new int[] { 3, 1 });
        keyPad.put("#", new int[] { 3, 2 });

        List<String> thumbs = new ArrayList<>();

        for (int number : numbers) {
            if (number == 1 || number == 4 || number == 7) {
                leftThumbLoc.replace(0, leftThumbLoc.length(), Integer.toString(number));
                thumbs.add("L");
            } else if (number == 3 || number == 6 || number == 9) {
                rightThumbLoc.replace(0, rightThumbLoc.length(), Integer.toString(number));
                thumbs.add("R");
            } else {
                int rightDist = manhattanDistance(keyPad.get(rightThumbLoc.toString()),
                        keyPad.get(Integer.toString(number)));
                int leftDist = manhattanDistance(keyPad.get(leftThumbLoc.toString()),
                        keyPad.get(Integer.toString(number)));

                if (rightDist < leftDist) {
                    thumbs.add("R");
                    rightThumbLoc.replace(0, rightThumbLoc.length(), Integer.toString(number));
                } else if (leftDist < rightDist) {
                    thumbs.add("L");
                    leftThumbLoc.replace(0, leftThumbLoc.length(), Integer.toString(number));
                } else {
                    if (hand.equals("right")) {
                        thumbs.add("R");
                        rightThumbLoc.replace(0, rightThumbLoc.length(), Integer.toString(number));
                    } else {
                        thumbs.add("L");
                        leftThumbLoc.replace(0, leftThumbLoc.length(), Integer.toString(number));
                    }
                }
            }
        }

        String answer = String.join("", thumbs);

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().solution(new int[] { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 }, "right"));
    }
}