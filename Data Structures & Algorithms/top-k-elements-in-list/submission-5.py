from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freqnums = defaultdict(int)
        topnums = []
        finalnums = []
        for n in nums:
            Freqnums[n] += 1
        sorted_pairs = sorted(Freqnums.items(), key = lambda x: x[1], reverse=True)
        for s in range(k):
            finalnums.append(sorted_pairs[s][0])
        return finalnums
