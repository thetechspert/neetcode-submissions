import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)


        for num in range(1, len(nums)):
            answer[num] = answer[num - 1] * nums[num - 1]

        temp_suffix = 1
        for num in reversed(range(len(nums))):
            answer[num] *= temp_suffix
            temp_suffix *= nums[num]


        return answer
