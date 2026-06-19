#Approach : Stack
#Time : O(n), Space : O(n)
# from collections import deque
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = deque()
#         for char in s :
#             if char == '{' or char == '[' or char == '(':
#                 stack.append(char)
#             else :
#                 if (len(stack) == 0): 
#                     return False
#                 if (char == '}') :
#                     if (stack.pop() != '{') :
#                         return False
#                 elif (char == ')') :
#                     if (stack.pop() != '(') :
#                         return False
#                 elif (char == ']') :
#                     if (stack.pop() != '[') :
#                         return False
#         if (len(stack) == 0) :
#             return True
#         return False
    

# s = Solution()
# str = "()[]{}"

# print(s.isValid(str))


#Approach : Stack
#Time : O(n), Space : O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s :
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else :
                if (len(stack) == 0): 
                    return False
                if (char == '}') :
                    if (stack.pop() != '{') :
                        return False
                elif (char == ')') :
                    if (stack.pop() != '(') :
                        return False
                elif (char == ']') :
                    if (stack.pop() != '[') :
                        return False
        if (len(stack) == 0) :
            return True
        return False
    

s = Solution()
str = "()[]{}"

print(s.isValid(str))