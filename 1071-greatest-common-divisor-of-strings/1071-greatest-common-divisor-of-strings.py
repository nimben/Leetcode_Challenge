class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        merged1 = ""
        merged2 = ""
        div = ""

        for i in range(min(len(str1), len(str2)), 0, -1):
            div = str1[:i]

            if len(str1) % len(div) == 0 and len(str2) % len(div) == 0:
                merged1 = div * (len(str1) // len(div))
                merged2 = div * (len(str2) // len(div))

                if merged1 == str1 and merged2 == str2:
                    return div

        return ""
