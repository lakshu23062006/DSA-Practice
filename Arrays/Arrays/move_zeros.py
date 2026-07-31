"""
Problem: Move Zeroes
Platform: LeetCode
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

nums = list(map(int, input("Enter array elements: ").split()))

j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print("Output:", nums)
