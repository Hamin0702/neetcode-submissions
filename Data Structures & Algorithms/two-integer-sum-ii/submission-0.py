class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers) - 1

        while start < end:
            twosum = numbers[start] + numbers[end]
        
            if twosum > target:
                end -= 1
            elif twosum < target:
                start += 1
            else:
                return [start + 1, end + 1]

        # for i, n in enumerate(numbers):
        #     search_num = target - n

        #     # binary search
        #     start = i + 1
        #     end = len(numbers)

        #     while start < end:
        #         mid = start + end // 2
        #         if numbers[mid] < search_num:
        #             start = mid
        #         elif numbers[mid] > search_num:
        #             end = mid
        #         else:   
        #             return [i + 1, mid + 1]
           
