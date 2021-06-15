class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt1 = 0
        
        for num in nums:
            cnt2 = 0
            while num >= 1:
                num /= 10
                cnt2 += 1
            
            if cnt2 % 2 == 0:
                cnt1 += 1
                
        return cnt1
