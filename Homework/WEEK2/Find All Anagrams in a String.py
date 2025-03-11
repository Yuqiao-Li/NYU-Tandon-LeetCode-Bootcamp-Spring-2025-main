class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        n, m = len(s), len(p)

        if n < m:
            return result
        
        p_counter = Counter(p)
 
        window_counter = Counter(s[:m])
        
        if window_counter == p_counter:
            result.append(0)
        
  
        for i in range(m, n):
            window_counter[s[i]] += 1
            window_counter[s[i-m]] -= 1
            if window_counter[s[i-m]] == 0:
                del window_counter[s[i-m]]
            
            if window_counter == p_counter:
                result.append(i - m + 1)
        
        return result