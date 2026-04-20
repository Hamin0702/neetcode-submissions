class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_list = [] 
        frequency_hashmap = defaultdict(int)
        frequency_list = [[] for _ in range(len(nums) + 1)]

        for number in nums:
            frequency_hashmap[number] += 1

        for number in frequency_hashmap:
            frequency_list[frequency_hashmap[number]].append(number)

        for i in range(len(nums), 0, -1):
            for n in frequency_list[i]:
                result_list.append(n)
                if len(result_list) == k:
                    return result_list
        return result_list