class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        hashset = set(nums)

        for i, n in enumerate(nums):
            
            if n - 1 not in hashset:

                val = n 
                seq = 0
                while val in hashset:
                    seq += 1
                    val += 1
                    
                res = max(res, seq)

        return res