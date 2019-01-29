# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

########################### Method 1 ###################################

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_set = set()
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None
        

########################### Method 2 ###################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        meet = None
        
        while fast:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            if fast == slow:
                meet = fast
                break
                
        while meet and head:
            if meet == head:
                return head
            meet = meet.next
            head = head.next
        return None
