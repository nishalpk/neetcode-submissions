class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                return [s[nums[i]],i]
            x = target - nums[i]
            s[x] = i
        