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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        int chg_len = n-m+1;
        ListNode *pre_head = NULL;
        ListNode *result   = head;
        while(--m){
            pre_head = head;
            head = head->next;
        }
        ListNode *new_tail = head;
        ListNode *new_head = NULL;
        while(head && chg_len){
            ListNode *next = head->next;
            head->next = new_head;
            new_head = head;
            head = next;
            chg_len--;
        }
        new_tail->next = head;
        if(pre_head){
            pre_head->next = new_head;
        }else{
            result = new_head;
        }
        return result;
    }
};
