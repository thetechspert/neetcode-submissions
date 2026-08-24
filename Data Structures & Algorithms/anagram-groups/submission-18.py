from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letter_to_idx = {
            'a':0, 'b':1, 'c':2, 'd':3,
            'e':4, 'f':5, 'g':6, 'h':7,
            'i':8, 'j':9, 'k':10, 'l':11,
            'm':12, 'n':13, 'o':14, 'p':15,
            'q':16, 'r':17, 's':18, 't':19,
            'u':20, 'v':21, 'w':22, 'x':23,
            'y':24, 'z':25
        }

        strings = defaultdict(list)
        print(0)
        for i in strs:
            counter = [0] * 26
            if i == "":
                strings[tuple(counter)].append(i)
                continue
            for letter in i:
                index = letter_to_idx[letter]
                counter[index] += 1
            strings[tuple(counter)].append(i)
        return list(strings.values())
