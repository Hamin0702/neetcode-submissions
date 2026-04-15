# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        while list1 != None or list2 != None:
            # Add the remaining linked list if one of them is empty
            if list1 == None:
                tail.next = list2
                break
            elif list2 == None:
                tail.next = list1
                break

            elif list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            elif list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next

        return dummy.next