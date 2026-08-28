class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        newcandies=[]
        for i in candies:
            newcandies.append(i+extraCandies)
        maximum = max(candies)
        for i in range(len(candies)):
            if newcandies[i] >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result