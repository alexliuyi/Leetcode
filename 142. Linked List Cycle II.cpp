/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 **************************** Method 1 ********************************
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
    std::set<ListNode*> node_set;
        while(head){
        if(node_set.find(head)!=node_set.end()){
            return head;
        }
        node_set.insert(head);
        head = head->next;   
        }
        return NULL;
    }
};

**************************** Method 2 ********************************
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast = head;
        ListNode *slow = head;
        ListNode *meet = NULL;
        
        while(fast){
            fast = fast->next;
            slow = slow->next;
            if(!fast){
                return NULL;
            }
            fast = fast->next;
            if(fast == slow){
                meet = fast;
                break;
            }
        }
        while(meet && head){
            if(meet==head){
                return head;
            }
            meet = meet->next;
            head = head->next;
        }
        return NULL;
    }
};
