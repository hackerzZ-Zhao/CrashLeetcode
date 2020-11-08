Question:
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # The method of detect cycle is the same as problem 141, we just need to do a little improvement
        # After we confirm there is a cycle in the linked list (when slow == fast)
        # We let slow pointer(or fast) point to head, let both pointers move forward for one step until they meet each other
        # the slow pointer would be head of the cycle
        if not head or not head.next:
            return
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # if no cycle, just return
        if fast != slow:
            return
        else:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
            

