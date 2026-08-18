# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2 is not None:
            return list2
        elif list2 is None and list1 is not None:
            return list1

        first_temp = list1
        second_temp = list2
        first_temp_prev = first_temp
        while first_temp != None and second_temp!= None:
            if first_temp.val == second_temp.val:
                prev_first_temp_next = first_temp.next
                prev_second_temp_next = second_temp.next
                first_temp.next = second_temp
                second_temp.next = prev_first_temp_next
                first_temp_prev = first_temp.next
                first_temp = prev_first_temp_next
                second_temp = prev_second_temp_next
            elif first_temp.val < second_temp.val:
                first_temp_prev = first_temp
                first_temp = first_temp.next
            else:
                if first_temp == list1:
                    prev_second_temp_next = second_temp.next
                    # first_temp_prev.next = second_temp
                    second_temp.next = first_temp
                    first_temp_prev = first_temp
                    first_temp = first_temp.next
                    second_temp = prev_second_temp_next
                else:
                    prev_second_temp_next = second_temp.next
                    first_temp_prev.next = second_temp
                    second_temp.next = first_temp
                    first_temp_prev = first_temp
                    first_temp = first_temp.next
                    second_temp = prev_second_temp_next
        
        if first_temp == None:
            while second_temp != None:
                prev_second_temp_next = second_temp.next
                first_temp_prev.next = second_temp
                second_temp.next = None
                second_temp = prev_second_temp_next
                first_temp_prev = first_temp_prev.next
        
        return list1
        

        