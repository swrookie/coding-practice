from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []

        self.backtrack(s, [], palindromes)

        return palindromes

    def backtrack(self, s, path, palindromes):
        if s == "":
            palindromes.append(path)
            print("added palindromes: ", palindromes)

        print("current s: ", s)

        for i in range(len(s)):
            sub_str = s[: i + 1]
            print("current substr: ", sub_str)
            if self.is_palindrome(sub_str):
                # path.append(sub_str)
                # print("currently added path: ", path)
                # self.backtrack(s[i + 1 :], path, palindromes)
                self.backtrack(s[i + 1 :], path + [sub_str], palindromes)
                # path.pop(len(path) - 1)
                # print("return to previous state: ", path)

    # Helper method
    def is_palindrome(self, s) -> bool:
        return s == s[::-1]


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
