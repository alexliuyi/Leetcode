class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        chg_len = int(n-m+1)
        
        pre_head = None
        result = head
        while m>1:
            m-=1
            pre_head = head
            head = head.next
            
        new_tail = head
        new_head = None
        
        while head and chg_len :
            new_next = head.next
            head.next = new_head
            new_head = head
            head = new_next
            chg_len-=1
        new_tail.next = head
        if pre_head:
            pre_head.next = new_head
        else:
            result = new_head
        return result
