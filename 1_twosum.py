Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


# Brute force : iterate over each element and check if the target - element is present in the array
# Time complexity : O(n^2) Space complexity : O(1)

# Optimized : use hashmap to store the value and its index
# Time complexity : O(n) Space complexity : O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #will store the value and its index
        for i,n in enumerate(nums):
            diff = target - n #calculate the diff
            if diff in hashMap: 
                return [hashMap[diff], i]
            hashMap[n] = i   




#Two Pointer approach - This will be used to solve the 3sum problem
# Only difference is that we need to return the indices and not the values
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Pair values with their indices and sort by value 
        nums_with_indices = [(val, idx) for idx, val in enumerate(nums)]
        nums_with_indices.sort()  # Sort by value
        
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                # Return original indices
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1