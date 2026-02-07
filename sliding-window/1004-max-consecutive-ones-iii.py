"""

1004. Max Consecutive Ones III

	Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

	Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
	Output: 6
	Explanation: [1,1,1,0,0,1,1,1,1,1,1]
		- Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

	Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
	Output: 10
	Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
	- Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

	- 1 <= nums.length <= 10^5
	- nums[i] is either 0 or 1.
	- 0 <= k <= nums.length

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize our left pointer, zero count and maximum length
        left, zero_count, max_len = 0, 0, 0

        # Loop through the nums, moving our right pointer until the end of the array
        for right in range(len(nums)):
            # The next number is a zero
            if nums[right] == 0:
                zero_count += 1

            # Advance the left pointer until the number of zeroes is less than or equal to k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Keep track of the maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len
