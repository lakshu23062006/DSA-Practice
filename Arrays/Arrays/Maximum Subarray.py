# LeetCode 53. Maximum Subarray

# Approach:
# 1. Initialize both current_sum and max_sum with the first element.
# 2. Traverse the array from the second element.
# 3. At each step, decide whether to start a new subarray or extend the current one.
# 4. Update the maximum subarray sum found so far.
# 5. Return the maximum sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
