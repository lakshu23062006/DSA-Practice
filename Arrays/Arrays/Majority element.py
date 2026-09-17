# Problem: Majority Element
# Approach: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Majority Element
def majority_element(nums):
count = 0
candidate = None
for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1
return candidate
nums = list(map(int, input("Enter the elements separated by spaces: ").split()))
result = majority_element(nums)
print("Majority Element:", result)
