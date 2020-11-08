Question:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # we set up two pointers:one slow, move one step in each loop, another is fast, move two steps in one loop
        # if there is not cycle, fast pointer will meet null and end the loop
        # if there is a cycle, fast pointer will meet slow pointer since fast move one more step in each loop
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
            
        return False
