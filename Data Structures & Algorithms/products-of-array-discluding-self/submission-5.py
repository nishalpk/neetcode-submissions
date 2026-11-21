class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1]*len(nums)
        pre = 1
        suf = 1
        for i in range(len(nums)):
            op[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            op[i] *= suf
            suf *= nums[i]
        return op
