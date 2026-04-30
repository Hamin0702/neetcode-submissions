class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums.sort()

        for i, n in enumerate(nums):

            if n > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            target = -n
            left = i + 1
            right = len(nums) -1

            while left < right:
                twosum = nums[left] + nums[right]
                if twosum < target:
                    left += 1
                elif twosum > target:
                    right -= 1
                else:
                    result.append([n, nums[left], nums[right]])
                    
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result