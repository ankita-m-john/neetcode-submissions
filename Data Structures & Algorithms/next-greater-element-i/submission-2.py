class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        idx = {num:i for i,num in enumerate(nums1)}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                index = idx[stack.pop()]
                res[index] = nums2[i]
            
            if nums2[i] in idx:
                stack.append(nums2[i])

        return res
