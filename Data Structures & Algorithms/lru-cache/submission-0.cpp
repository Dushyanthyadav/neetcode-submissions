class LRUCache {
private:
    struct Node {
        int key;
        int val;
        Node* prev;
        Node* next;
        Node(int k, int v): key(k), val(v), prev(nullptr), next(nullptr) {}
    };
    int cap;
    std::unordered_map<int, Node*> hash;
    Node* head;
    Node* tail;

    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insertAtTail(Node* node) {
        node->prev = tail->prev;
        node->next = tail;
        tail->prev->next = node;
        tail->prev = node;
    }

    void moveToTail(Node* node) {
        removeNode(node);
        insertAtTail(node);
    }
public:
    LRUCache(int capacity): cap(capacity) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    ~LRUCache() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
    
    int get(int key) {
        auto it = hash.find(key);
        if (it == hash.end()) {
            return -1;
        }
        Node* node = it->second;
        moveToTail(node);
        return node->val;
    }
    
    void put(int key, int value) {
        auto it = hash.find(key);
        if (it != hash.end()) {
            Node* node = it->second;
            node->val = value;
            moveToTail(node);
            return;
        }

        if (hash.size() == cap) {
            Node* lru = head->next;
            removeNode(lru);
            hash.erase(lru->key);
            delete lru;
        }

        Node* newNode = new Node(key, value);
        insertAtTail(newNode);
        hash[key] = newNode;
    }
};
