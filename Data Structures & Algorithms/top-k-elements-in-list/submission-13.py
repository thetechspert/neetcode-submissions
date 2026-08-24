from itertools import chain
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

        return list(chain.from_iterable(reversed(buckets)))[:k]