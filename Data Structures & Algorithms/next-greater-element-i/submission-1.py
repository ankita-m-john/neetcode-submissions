class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1) 
        #Hash map for index lookup
        idx = { num : i for i, num in enumerate(nums2)}

        for i in range(len(nums1)):
            for j in range(idx[nums1[i]],len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    print(res,nums1[i],nums2[j])
                    break
        return res