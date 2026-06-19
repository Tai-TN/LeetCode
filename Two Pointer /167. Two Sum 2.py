"""
Given a 1-indexed array of integers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific number. Let these two numbers be and where .numberstargetnumbers[index1]numbers[index2]1 <= index1 < index2 <= numbers.length

Return the indices of the two numbers  and , each incremented by one, as an integer array of length 2.index1index2[index1, index2]

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftPointer = 0
        rightPointer = len(numbers) - 1
        resultList = []
        while (leftPointer < rightPointer) :
            total = numbers[leftPointer] + numbers[rightPointer]
            if (total == target):
                resultList = [leftPointer + 1, rightPointer + 1]
                return resultList
            elif total < target :
                leftPointer += 1
            else :
                rightPointer -= 1
        return resultList



numbers = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(numbers, target))
        