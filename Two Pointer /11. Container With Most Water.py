from typing import List


class Solution(object):
    def BruteForce(self, nums : List[int]):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maxArea = 0
        for i in range(1, len(nums)):
            for j in range (0, i):
                current = (i - j )* min(nums[i], nums[j])
                maxArea = max(current, maxArea)

        return maxArea


    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        leftPointer = 0
        rightPointer = len(nums) - 1
        while (leftPointer < rightPointer) :
            maxArea = max((rightPointer - leftPointer)* min(nums[leftPointer], nums[rightPointer]), maxArea)
            if (nums[leftPointer] < nums[rightPointer]):
                leftPointer += 1
            else :
                rightPointer -=1
        return maxArea


solution = Solution()
nums = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(nums))