class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_singles = set()
        for i in range(len(nums)):
            if nums[i] not in check_singles:
                check_singles.add(nums[i])
            else:
                return True
        return False