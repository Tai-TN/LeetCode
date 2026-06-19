# Approach : Dictionary
#Time : O(n), Space : O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        my_dict = {}
        for i, num in enumerate(nums) :
            if (my_dict.get(target - num) != None):
                result.append(my_dict.get(target - num))
                result.append(i)
                break
            else:
                my_dict[num] = i
        return result
    
s = Solution()
nums = [1, 2, 5, 7]
target = 9
print(s.twoSum(nums, target))

            