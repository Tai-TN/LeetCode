"""
Given two strings s and p, return an array of all the start indices of p's in s. You may return the answer in any order.
Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

 

Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        indices = []
        if (len(p) > len(s)):
            return indices
        p_count = [0]*26
        s_count = [0]*26
        for i in range(0, len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
        
        for i in range(0, len(p)):
            s_count[ord(s[i]) - ord('a')] += 1
            if (p_count == s_count):
                indices.append(left)
                
                
        for i in range(len(p), len(s)):
            s_count[ord(s[left]) - ord('a')] -= 1
            left += 1
            s_count[ord(s[i]) - ord('a')] += 1
            if p_count == s_count:
                indices.append(left)
                
        return indices
            

    
S = Solution()
s = "cbaebabacd"
p = "abc"
print(S.findAnagrams(s, p))
