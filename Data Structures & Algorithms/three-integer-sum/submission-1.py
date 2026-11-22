class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        f = defaultdict(int)
        for i in nums:
            f[i] +=1
        
        for i in range(len(nums)):
            f[nums[i]] -=1
            if i and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                f[nums[j]] -=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                
                t=-(nums[i]+nums[j])
                # t= -t
                if f[t]>0:
                    res.append([nums[i],nums[j],t])
            for j in range(i+1,len(nums)):
                f[nums[j]] +=1
        return res
                
        