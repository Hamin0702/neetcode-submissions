class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            check =  (end - start) // 2 + start

            if nums[check] == target:
                return check
            elif nums[check] < target:
                start = check + 1
            elif nums[check] > target:
                end = check - 1

        return -1