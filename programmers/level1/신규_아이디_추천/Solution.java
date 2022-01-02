// package programmers.level1.신규_아이디_추천;

import java.lang.StringBuilder;

public class Solution {
    public String solution(String new_id) {
        String answer = "";

        // 1단계
        // 모든 대문자를 대응되는 소문자로 치환
        new_id = new_id.toLowerCase();

        // 2단계
        // 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        new_id = new_id.replaceAll("[^a-z0-9\\-\\_\\.]", "");

        // 3단계
        // 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
        new_id = new_id.replaceAll("[\\.]{2,}", ".");

        // 4단계
        // 마침표(.)가 처음이나 끝에 위치한다면 제거
        if (new_id.startsWith(".") || new_id.endsWith("."))
            new_id = new_id.replaceAll("^[.]|[.]$", "");

        // 5단계
        // 빈 문자열이라면, new_id에 "a"를 대입
        if (new_id.length() == 0)
            new_id += "a";

        // 6단계
        // 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        // 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if (new_id.length() >= 16) {
            new_id = new_id.substring(0, 15);
            if (new_id.endsWith("."))
                new_id = new_id.replaceAll(".$", "");
        }

        // 7단계 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙인다
        if (new_id.length() <= 2) {
            StringBuilder sb = new StringBuilder(new_id);
            String lastStr = new_id.substring(new_id.length() - 1);

            while (sb.length() < 3) {
                sb.append(lastStr);
            }
            new_id = sb.toString();
        }

        answer = new_id;

        return answer;
    }

    public static void main(String[] args) {
        String new_id = "...!@BaT#*..y.abcdefghijklm";
        System.out.println(new Solution().solution(new_id));
    }
}
