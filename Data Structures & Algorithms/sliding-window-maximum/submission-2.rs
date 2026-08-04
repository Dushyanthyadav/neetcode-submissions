impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut heap = BinaryHeap::new();
        let mut output = Vec::with_capacity(nums.len() - k + 1);

        for i in 0..nums.len() {
            heap.push((nums[i], i));
            if i >= k - 1 {
                while heap.peek().unwrap().1 + k <= i {
                    heap.pop();
                }
                output.push(heap.peek().unwrap().0);
            }
        }

        output
    }
}