class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        word_2 = {}
        for i in range(len(s)):
            if s[i] not in word_1:
                word_1[s[i]] = 1 
            else:
                word_1[s[i]] += 1
        for l in range(len(t)):
            if t[l] not in word_2:
                word_2[t[l]] = 1 
            else:
                word_2[t[l]] += 1
        if word_1 == word_2:
            return True
        else:
            return False
            
            

