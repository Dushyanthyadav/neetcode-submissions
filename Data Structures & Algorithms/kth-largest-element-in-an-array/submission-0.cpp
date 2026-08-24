class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
       priority_queue<int> maxHeap;
       for(auto num: nums) {
            maxHeap.push(num);
       } 
        if (k == 1) {
            return maxHeap.top();
        }

        while (true) {
            if (k == 1) {
                return maxHeap.top();
            }
            maxHeap.pop();
            k--;
        }

        return -1;
    }        
};
