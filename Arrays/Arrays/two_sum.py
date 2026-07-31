"""
Problem: Two Sum
Platform: LeetCode
Approach: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

nums = list(map(int, input().split()))
target = int(input())

d = {}

for i in range(len(nums)):
    x = target - nums[i]
    if x in d:
        print([d[x], i])
        break
    d[nums[i]] = i
