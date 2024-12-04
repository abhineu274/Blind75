53. Maximum Subarray
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Normal approach: 
Time complexity : O(n^3) Space complexity : O(1)



Optimal approach: Kadane's algorithm
Time complexity : O(n) Space complexity : O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], 0
        for num in nums:
            if curr_sum < 0:    #if the current sum is negative, we reset it to 0 - thats it
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum
        