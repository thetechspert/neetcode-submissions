import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)


        for num in range(1, len(nums)):
            prefix_prod[num] = nums[num - 1] * prefix_prod[num - 1]          

        temp_suffix = 1
        for s in reversed(range(len(nums))):
            suffix_prod[s] = temp_suffix
            temp_suffix *= nums[s]

        for i in range(len(nums)):
            answer[i] = (prefix_prod[i] * suffix_prod[i])

        return answer
