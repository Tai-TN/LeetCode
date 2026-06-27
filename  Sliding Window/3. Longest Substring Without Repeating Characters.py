"""
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        temp = []
        current_length = 0

        for right in range(0, len(s)):
            if s[right] not in temp:
                temp.append(s[right])
            else:
                max_length = max(max_length, len(temp))
                while s[right] in temp:
                    temp.remove(s[left])
                    left += 1
                temp.append(s[right])
        max_length = max(max_length, len(temp))

        return max_length


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
