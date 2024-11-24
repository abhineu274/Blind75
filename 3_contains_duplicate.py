217. Contains Duplicate
Solved
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109







#Optimal solution using set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_set = set()
        for n in nums:
            if n in val_set:
                return True
            val_set.add(n)
        return False


#Brute force solution
# for n in range(0, len(nums)): #n is an index here
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in range(0, len(nums)):
            for m in range(n+1, len(nums)):
                if nums[n]==nums[m]:
                    return True
        return False
