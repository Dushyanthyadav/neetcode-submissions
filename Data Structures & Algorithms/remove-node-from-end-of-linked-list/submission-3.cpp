/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        vector<ListNode*> v;
        ListNode *a = head;

        while (a != nullptr) {
            v.push_back(a);
            a = a->next;
        }

        int j = v.size() - n;

        if (j == 0) {
            return head->next;
        }
        
        v[j-1]->next = v[j]->next;

        return head;
    }
};