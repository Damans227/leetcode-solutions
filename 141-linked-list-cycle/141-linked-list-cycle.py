# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # Optimized solution using Floyds tortoise and hare algorithm
        while fast and fast.next:
            slow = slow.next # Address of the next node in Linked list 
            fast = fast.next.next # Address of the next to next node in Linked list 
            if slow == fast:
                return True
        
        return False