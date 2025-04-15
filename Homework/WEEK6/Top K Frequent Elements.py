class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)
        

        result = []
        for i in range(len(freq) - 1, 0, -1):
            result.extend(freq[i])
            if len(result) >= k:
                return result[:k]
        
        return result