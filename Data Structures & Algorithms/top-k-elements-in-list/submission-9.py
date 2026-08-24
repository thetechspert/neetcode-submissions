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
        
        clean_buckets = list(filter(lambda bucket: len(bucket) > 0, buckets))

        for s in reversed(clean_buckets):
            for num in s:
                final.append(num)
                if len(final) == k:
                    return final
