class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr,su = [1],[1]
        op = [1]*len(nums)
        # j,k = 1
        for i in range(len(nums)):
            pr.append(nums[i]*pr[i])
            # j = pr[i]
            # print(len(nums)-i)
            su.append(nums[len(nums)-i-1]*su[i])
            # k = su[i]

        pr = pr[::]
        su = su[:-1:]
        su = su[::-1]
        # print(pr,su)
        for i in range(len(nums)):
            op[i] = pr[i]*su[i]
        return op