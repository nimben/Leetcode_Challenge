class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=c=0
        for num in nums:
            if num %6 == 0 :
                sum+=num
                c+=1
        return sum//c if c else 0
        
        