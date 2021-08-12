class Solution:
    def longestPalindrome(self, s: str) -> str:
        from itertools import combinations as cm
        palindromes = []
        s = s.lower()
        if s == s[::-1]:
            return s
        else:
            substrings = [s[i:j] for i, j in cm(range(len(s) + 1), 2)]
            for sub in substrings:
                if sub == sub[::-1]:
                    palindromes.append(sub)
            return max(palindromes, key=len)


sol = Solution()
print(sol.longestPalindrome('babad'))
