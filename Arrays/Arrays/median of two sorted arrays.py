# LeetCode 4. Median of Two Sorted Arrays

# Approach:
# 1. Merge both sorted arrays.
# 2. Sort the merged array.
# 3. If the total number of elements is odd, return the middle element.
# 4. If the total number of elements is even, return the average of the two middle elements.

# Time Complexity: O((n + m) log(n + m))
# Space Complexity: O(n + m)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()

        n = len(num)

        if n % 2 == 1:
            return num[n // 2]
        else:
            return (num[n // 2 - 1] + num[n // 2]) / 2.0
