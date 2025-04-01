class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        
        dp = [0] * (n + 1)
        dp[1] = 1  
        

        sharing = 0
        
       
        for i in range(2, n + 1):
            if i - delay >= 1:
                sharing = (sharing + dp[i - delay]) % MOD
                
            if i - forget >= 1:
                sharing = (sharing - dp[i - forget] + MOD) % MOD
            dp[i] = sharing
        
        # Count all people who know the secret at the end of day n
        result = 0
        for i in range(max(1, n - forget + 1), n + 1):
            result = (result + dp[i]) % MOD
            
        return result