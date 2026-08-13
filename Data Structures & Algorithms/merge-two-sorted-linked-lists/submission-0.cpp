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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode merge(0);
        ListNode *head = &merge;
        ListNode *a = list1;
        ListNode *b = list2;
        while (a != nullptr and b != nullptr) {
            if (a->val <= b->val) {
               head->next = a;
                a = a->next;
            } else {
                head->next = b;
                b = b->next;
            }

            head = head->next;
        }

        if (a != nullptr) {
            head->next = a;
        }

        if (b != nullptr) {
            head->next = b;
        }

        return merge.next;
    }
};
