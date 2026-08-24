class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        correctnums = []
        for num in range(len(nums)):
            for numtwo in range(len(nums)):
                if numtwo == num:
                    continue
                if nums[num] + nums[numtwo] == target:
                    if num > numtwo:
                        correctnums.append(numtwo)
                        correctnums.append(num)
                        return correctnums
                    else:
                        correctnums.append(num)
                        correctnums.append(numtwo)
                        return correctnums

    
    
        

