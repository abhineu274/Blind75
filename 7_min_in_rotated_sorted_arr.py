153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.









If you see O(log n) time complexity, think of binary search.
Just take 3 pointers - left, right and mid (l, m, r).

Keep playing with them.
There can be 8 combinations of l, m, r. But you don't have to worry about all of them.

You just need to check if the mid is part of left sorted grouping or the right sorted grouping.

[6, 7, 1, 2, 3, 4, 5]  - Play with this example to understand the logic.
Here mid is 2 and it is less than the right.




Optimal Solution: Binary search
Key Observations ->
Sorted Part: In a rotated array, at least one part (left or right) is always sorted.

Binary Search:
If the middle element is greater than the last element, the minimum must be in the right part.
If the middle element is smaller than the last element, the minimum is in the left part or at mid.




class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            # Check if the minimum is in the right part
            if nums[mid] > nums[end]:
                start = mid + 1
            else:  # Minimum is in the left part or at mid
                end = mid
        
        # When the loop ends, start == end
        return nums[start]
            


        