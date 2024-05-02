from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations=[]
        dic={}
        string_words="".join(chr(x) for x in range(97,123))
        ind=0
        for i in range(2,10):
            if i==7 or i== 9:
                dic[str(i)]=string_words[ind:ind+4]
                ind+=4
            else:
                dic[str(i)]=string_words[ind:ind+3]
                ind+=3
        def backtracking(index,path):
            if index ==len(digits):
                combinations.append("".join(path))
                return
            letters = dic[digits[index]]

            for letter in letters:
                path.append(letter)
                backtracking(index+1,path)
                path.pop()

        backtracking(0,[])
        return combinations

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
