class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        for i in range(len(s)):
            if s[i] not in word_1:
                word_1[s[i]] = 1 
            else:
                word_1[s[i]] += 1
        for l in range(len(t)):
            if t[l] in word_1:
                word_1[t[l]] -= 1
            else: 
                return False
        for letter in word_1:
            if word_1[letter] != 0:
                return False
        return True
            
