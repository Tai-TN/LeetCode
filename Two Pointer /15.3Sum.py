from typing import List

# Xử lý trùng lặp khá khó
# Time O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultList = []
        nums.sort()
        for i in range(len(nums)-2):
            leftPointer = i + 1
            rightPointer = len(nums) - 1
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            while (leftPointer < rightPointer):
                currentSum = nums[i] + nums[leftPointer] + nums[rightPointer]
                if (currentSum == 0):
                    resultList.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    rightPointer -= 1
                    while (leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer-1]):
                        leftPointer +=1
                    while (leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer+1]):
                        rightPointer -=1
                elif currentSum < 0 :
                    leftPointer += 1
                else :
                    rightPointer -= 1
        return resultList
                    


nums = [-1,0,1,2,-1,-4]
# [-1, -1, 0, 1, 2 ,4]
# nums = [0, 0, 0, 0]
solution = Solution()
result = solution.threeSum(nums)
print(result)



