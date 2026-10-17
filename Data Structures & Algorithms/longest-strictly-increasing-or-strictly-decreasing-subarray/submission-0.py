class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_dec, var = 1, 1
        length = len(nums)
        if length == 1:
            return 1

        for i in range(1,length):
            if nums[i] < nums[i-1]:
                var += 1
            else:
                var = 1
            if var > longest_dec:
                longest_dec = var
        
        longest_inc, var = 1, 1
        for i in range(1,length):
            if nums[i] > nums[i-1]:
                var += 1
            else:
                var = 1
            if var > longest_inc:
                longest_inc = var
        
        return max(longest_inc,longest_dec)
           
