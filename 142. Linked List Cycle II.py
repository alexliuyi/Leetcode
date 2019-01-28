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
