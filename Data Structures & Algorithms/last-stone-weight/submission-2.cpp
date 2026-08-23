class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;

        for (int num: stones) {
            maxHeap.push(num);
        }
    
        if (maxHeap.size() == 1) {
            return maxHeap.top();
        }

        while (maxHeap.size() > 1) {
            int x = maxHeap.top();
            maxHeap.pop();
            int y = maxHeap.top();
            maxHeap.pop();
            
            if (x == y) {
                continue;
            } else {
                maxHeap.push(x-y);
            }
        } 

        if (maxHeap.size() == 0) {
            return 0;
        }


        return maxHeap.top();
        
    }
};
