class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [] 
        frequency_hashmap = defaultdict(int)
        frequency_list = [[] for i in range(len(nums) + 1)]

        for number in nums:
            frequency_hashmap[number] += 1

        for number in frequency_hashmap:
            frequency_list[frequency_hashmap[number]].append(number)

        for i in range(len(nums), 0, -1):
            for n in frequency_list[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result