class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        numticker = 0
        num = []
        for i in range(len(nums)):
            possiblesolution = target - nums[i]
            if possiblesolution in hashmap:
                if hashmap[possiblesolution] != i:
                    num.append(min(i,nums.index(possiblesolution)))
                    num.append(max(i,nums.index(possiblesolution)))
                    return num
            hashmap[nums[i]] = numticker
            numticker += 1