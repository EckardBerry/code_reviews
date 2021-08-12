class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_string = ''
        for char in s:
            if char not in new_string:
                new_string += char
        return len(new_string)




sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('bbbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring(''))