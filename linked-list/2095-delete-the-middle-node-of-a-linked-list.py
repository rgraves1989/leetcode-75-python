"""

2095. Delete the Middle Node of a Linked List

    You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:

    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]
    Explanation:
        - The above figure represents the given linked list. The indices of the nodes are written below.
        - Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
        - We return the new list after removing this node. 

Example 2:

    Input: head = [1,2,3,4]
    Output: [1,2,4]
    Explanation:
        - The above figure represents the given linked list.
        - For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:

    Input: head = [2,1]
    Output: [2]
    Explanation:
        - The above figure represents the given linked list.
        - For n = 2, node 1 with value 1 is the middle node, which is marked in red.
        - Node 0 with value 2 is the only node remaining after removing node 1.
 
Constraints:

    - The number of nodes in the list is in the range [1, 10^5].
    -1 <= Node.val <= 10^5

"""


# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Loop through the linked list building an in-memory list of nodes and track the length
        curr_node, node_list, list_len = head, [], 0
        while curr_node:
            node_list.append(curr_node)
            curr_node = curr_node.next
            list_len += 1

        # Determine which node we need to delete
        delete_node_index = floor(list_len / 2)

        # Find the previous and next nodes from the one we are deleting
        left_node = (
            node_list[delete_node_index - 1] if delete_node_index - 1 >= 0 else None
        )
        right_node = (
            node_list[delete_node_index + 1]
            if delete_node_index + 1 < list_len
            else None
        )

        if not left_node and right_node:
            # No left node, meaning the deleted node was the head
            head = rigth_node
        elif left_node and not right_node:
            # No right node, meaning the delete node was the tail
            left_node.next = None
        elif left_node and right_node:
            # Left and right nodes exists, point the left node to the right now
            left_node.next = right_node
        else:
            # No left or right nodes, this was the only node
            return None

        return head
