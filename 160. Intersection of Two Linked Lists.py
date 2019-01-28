# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#/***************     Methon 1 ******************/


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_set = set()
        while headA!=None:
            node_set.add(headA)
            headA = headA.next
        while headB!=None:
            if headB in node_set:
                return headB
            headB = headB.next
        return None
        
        
#/***************     Methon 2 ******************/

def get_list_length(head):
    length = 0
    while head!=None:
        length+=1
        head = head.next
    return length

def forward_long_list(long_len, short_len, head):
    delta = long_len - short_len
    while head and delta:
        head = head.next
        delta-=1
    return head

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        list_A_len = get_list_length(headA)
        list_B_len = get_list_length(headB)
        if list_A_len > list_B_len:
            headA = forward_long_list(list_A_len, list_B_len, headA)
        else:
            headB = forward_long_list(list_B_len, list_A_len, headB)
        while headA and headB:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
