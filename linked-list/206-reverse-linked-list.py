"""

206. Reverse Linked List

	Given the head of a singly linked list, reverse the list, and return the reversed list

Example 1:

	Input: head = [1,2,3,4,5]
	Output: [5,4,3,2,1]

Example 2:

	Input: head = [1,2]
	Output: [2,1]

Example 3:

	Input: head = []
	Output: []

Constraints:

	- The number of nodes in the list is the range [0, 5000].
	- -5000 <= Node.val <= 5000

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node, last_node, rev_head = head, None, None

        # Traverse the linked list
        while curr_node:
            # If the current node doesn't have a next node, this is the new head
            if not curr_node.next:
                rev_head = curr_node

            # Save our next node, before we assign the last node to the current node's next pointer
            next_node = curr_node.next
            if not last_node:
                curr_node.next = None
            else:
                curr_node.next = last_node

            # Advance nodes
            last_node = curr_node
            curr_node = next_node

        return rev_head
