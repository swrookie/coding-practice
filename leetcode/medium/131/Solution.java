import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r))
                return false;
        }

        return true;
    }

    public void backTrack(String s, List<String> path, List<List<String>> palindromes) {
        if (s.equals("")) {
            palindromes.add(path);
            System.out.println("added palindromes: " + path);
        }

        System.out.println("Current s: " + s);

        for (int i = 0; i < s.length(); i++) {
            String subString = s.substring(i, i + 1);
            System.out.println("current substring: " + subString);
            if (isPalindrome(subString)) {
                System.out.println("substring is palindrome");
                path.add(subString);
                System.out.println("substring added to path: " + path);
                backTrack(s.substring(i + 1, s.length()), path, palindromes);
                path.remove(path.size() - 1);
                System.out.println("substring removed from path: " + path);
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<List<String>> palindromes = new ArrayList<>();
        List<String> path = new ArrayList<>();

        backTrack(s, path, palindromes);

        return palindromes;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().partition("aab"));
    }
}
