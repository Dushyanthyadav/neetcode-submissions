class Solution {
public:
    unordered_map<Node*, Node*> map;

    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        if (map.count(head)) return map[head];

        Node* copy = new Node(head->val);
        map[head] = copy;
        copy->next = copyRandomList(head->next);
        copy->random = map[head->random];
        return copy;
    }
};
