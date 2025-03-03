class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * (n + 1)  
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):  
            suffix[i] = suffix[i + 1] * nums[i]
        answer =[0]* n 
        for i in range(n):
            if i==0 :
                answer[i] = suffix[i+1]
            else:
                answer[i] = prefix[i]*suffix[i + 1]

        return answer

        

           
        