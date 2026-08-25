
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            x = string 
            string = x + str(len(i)) + "#" + i  
        return string
    def decode(self, s: str) -> List[str]:
        solution = []
        counter = 0
        while counter < len(s):
            j = counter
            while s[j] != "#":
                j += 1

            length = int(s[counter: j])
            print(length)
            solution.append(s[j + 1: j + 1 + length])
            counter = j + 1 + length
        return solution

