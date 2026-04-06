class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {} #hashmap with number value : index in array

        for i in range(len(nums)):
            target_final = target - nums[i]
            if target_final in indices:
                if i < indices[target_final]:
                    return [i,indices[target_final]]
                else:
                    return [indices[target_final],i]

            indices[nums[i]] = i
        #return two indices that add up to target
        #nums[i] + nums[j] == target
        #i != j

        #look at nums[i], look for target - nums[j]
        