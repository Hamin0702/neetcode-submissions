class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numList = {}
        for i in range(len(nums)):
            if nums[i] in numList:
                return True
            else:
                numList[nums[i]] = True

        return False
        