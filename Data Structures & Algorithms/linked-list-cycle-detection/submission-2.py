# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head

        while slow.next is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        # node_set = set()
        # node_set.add(head)
        # temp = head
        # while temp.next is not None:
        #     temp = temp.next
        #     if temp in node_set:
        #         return True
        #     else: node_set.add(temp)
        return False
