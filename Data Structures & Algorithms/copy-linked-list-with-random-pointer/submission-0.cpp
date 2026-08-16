/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        vector<Node *> v;

        if (head == NULL) {
            return head;
        }

        Node *cur = head;
        unordered_map<Node*, int> hash;
        int i = 0;
        while (cur != NULL) {
            v.push_back(cur);
            hash.insert({cur, i});
            cur = cur->next;
            i++;
        }
        Node *other = new Node(v[0]->val);
        Node *temp = other;
        vector<Node *> u;
        u.push_back(other);
        for (int j = 1; j < v.size(); j++) {
            temp = other;
            other = new Node(v[j]->val);
            temp->next = other;
            u.push_back(other);
        }

        Node* tmp = u[0];
        Node* result = tmp;
        i = 0;
        while (tmp != NULL) {
            if (v[i]->random != NULL) {
                int index = hash[v[i]->random];
                tmp->random = u[index];
            } else {
                tmp->random = NULL;
            }
            tmp = tmp->next;
            i++;
        }


        return result;
        
    }
};
