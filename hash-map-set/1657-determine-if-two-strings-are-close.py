"""

1657. Determine if Two Strings Are Close

	Two strings are considered close if you can attain one from the other using the following operations:

	Operation 1: Swap any two existing characters.
		- For example, abcde -> aecdb
	Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
		- For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
		- You can use the operations on either string as many times as necessary.

	Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

	Input: word1 = "abc", word2 = "bca"
	Output: true
	Explanation: You can attain word2 from word1 in 2 operations.
		- Apply Operation 1: "abc" -> "acb"
		- Apply Operation 1: "acb" -> "bca"

Example 2:

	Input: word1 = "a", word2 = "aa"
	Output: false
	Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

	Input: word1 - = "cabbba", word2 = "abbccc"
	Output: true
	Explanation: - You can attain word2 from word1 in 3 operations.
		- Apply Operation 1: "cabbba" -> "caabbb"
		- Apply Operation 2: "caabbb" -> "baaccc"
		- Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

	- 1 <= word1.length, word2.length <= 10^5
	- word1 and word2 contain only lowercase English letters.

"""


# Time complexity: O(N+M)
# Space complexity: O(N+M)
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If strings have different lenght, return False
        if len(word1) != len(word2):
            return False

        # Get the character counts for word1 and word2
        w1_counts = Counter(word1)
        w2_counts = Counter(word2)

        # If the strings have different sets of letters, return False
        if set(w1_counts.keys()) != set(w2_counts.keys()):
            return False

        # Sort the counts and compare, if not equal word1 can not be transformed into word2
        if sorted(w1_counts.values()) != sorted(w2_counts.values()):
            return False

        # Check passed, word1 can be transformed into word2 using the operations
        return True
