class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                continue
            if i and nums[i]==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                if l>i+1 and nums[l]==nums[l-1]:
                    l+=1
                    continue
                # if r!=len(nums)-1 and nums[r]==nums[r+1]:
                #     r-=1
                #     continue
                t = nums[i]+nums[l]+nums[r]
                if t<0:
                    l+=1
                elif t>0:
                    r-=1
                elif t==0:
                   res.append([nums[i],nums[l],nums[r]])
                   l+=1
                   r-=1
                # print(l,r)
        return res 