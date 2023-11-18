# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

-- Create temporary variable to store the next node
-- Change the next node pointer to the previous node
-- Assign the previous with the current and the current with the next

The time complexity: O(n), The space complexity: O(1)

"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev # 'prev' now points to the new head of the reversed list