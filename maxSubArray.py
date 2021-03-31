class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #DP solution to LC 53 
        
        dp = [0]*len(nums)
        
        for index, value in enumerate(nums):
            
            dp[index] = max(dp[index-1] + value, value) 
            
        return max(dp)
     
        #sumOf = 0
        #minVal = 0 
        #result = nums[0] 
        #
        #for i in nums:
        #    
        #    sumOf+= i 
        #    
        #   if (sumOf - minVal > result):
        #        result = sumOf - minVal 
        #    
        #    if (sumOf < minVal): 
        #        minVal = sumOf
        #    
        #return result 
