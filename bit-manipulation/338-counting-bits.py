"""

338. Counting Bits

	Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

	Input: n = 2
	Output: [0,1,1]
	Explanation:
		- 0 --> 0
		- 1 --> 1
		- 2 --> 10

Example 2:

	Input: n = 5
	Output: [0,1,1,2,1,2]
	Explanation:
		- 0 --> 0
		- 1 --> 1
		- 2 --> 10
		- 3 --> 11
		- 4 --> 100
		- 5 --> 101
 
Constraints:

	- 0 <= n <= 10^5

"""


# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        sequence, sequence_ptr, sequence_len = [0, 1], 0, 2

        # Loop through each 0 <= index <= n, incrementing a sequence index counter
        for index in range(n + 1):
            sequence_ptr += 1

            # End of the sequence, extend from here
            if sequence_ptr == sequence_len:
                sequence.extend([val + 1 for val in sequence])
                sequence_len *= 2

        # Truncate the sequence array to our desired output length (n + 1)
        return sequence[: n + 1]
