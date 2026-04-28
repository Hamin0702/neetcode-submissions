class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        pref = 1
        for i, n in enumerate(nums):
            output[i] = pref
            pref *= n

        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suf
            suf *= nums[i]

        return output