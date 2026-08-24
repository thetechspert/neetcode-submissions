from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        final = []
        Freqnums = defaultdict(int)
        buckets = [[] for s in range(len(nums) + 1)]

        for n in nums:
            Freqnums[n] += 1

        for i in Freqnums:
            buckets[Freqnums[i]].append(i)

        for s in reversed(buckets):
            if len(s) == 0:
                continue
            for num in s:
                final.append(num)
                if len(final) == k:
                    return final
