class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, cur = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] or ((nums[i-cur] < nums[i-cur+1]) != (nums[i-1] < nums[i])):
                cur = 1 if (nums[i] == nums[i-1]) else 2
                continue
            cur += 1
            res = max(res,cur)

        return res