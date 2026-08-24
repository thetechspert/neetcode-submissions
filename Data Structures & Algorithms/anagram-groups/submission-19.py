from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strings = defaultdict(list)
        print(0)
        for i in strs:
            counter = [0] * 26
            if i == "":
                strings[tuple(counter)].append(i)
                continue
            for letter in i:
                index = ord(letter) - ord("a")
                counter[index] += 1
            strings[tuple(counter)].append(i)
        return list(strings.values())
