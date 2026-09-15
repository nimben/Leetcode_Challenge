class Solution:
    def reverseWords(self, s: str) -> str:
       words = s.split()
       words = words[::-1]
       res = " ".join(words)
       return(res)
        
        