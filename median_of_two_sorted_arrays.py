class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return (sum(nums1) + sum(nums2))/(len(nums1) + len(nums2))

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2, 7]))