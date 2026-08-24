class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        numticker = 0
        num = []
        for i in range(len(nums)):
            print(4)
            possiblesolution = target - nums[i]
            if possiblesolution in hashmap:
                print(3)
                if hashmap[possiblesolution] != i:
                    print(1)
                    num.append(min(i,nums.index(possiblesolution)))
                    num.append(max(i,nums.index(possiblesolution)))
                    return num
            print(5)           
            hashmap[nums[i]] = numticker
            numticker += 1
            

                        
                

                

