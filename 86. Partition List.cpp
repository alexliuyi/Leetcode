/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode less_head(0);
        ListNode more_head(0);
        ListNode *less_pre = &less_head;
        ListNode *more_pre = &more_head;
        while(head){
            if(head->val < x){
                less_pre->next = head;
                less_pre=head;
            }else{
                more_pre->next = head;
                more_pre = head;
            }
            head = head->next;
        }
        less_pre->next = more_head.next;
        more_pre->next = NULL;
        return less_head.next;
    }
};
