class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        temp=""
        s=list(s)
        while(i<j):
            while i < j and s[i] not in "aeiouAEIOU":
                i += 1
            
            while i < j and s[j] not in "aeiouAEIOU":
                j -= 1

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i+=1
            j-=1
            
        s = "".join(s)
        return s
        