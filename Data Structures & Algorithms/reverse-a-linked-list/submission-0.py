# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        curr = head.next
        prev = head
        while curr.next != None:
            # print(f"Entered loop for prev: {prev.val} and curr: {curr.val}")
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        head.next = None
        head = curr

        return head



        