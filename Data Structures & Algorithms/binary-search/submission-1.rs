impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l: i32 = 0;
        let mut h: i32 = nums.len() as i32 - 1;

        while l <= h {
            let mid = l + (h-l)/2;
            if nums[mid as usize] == target {
                return mid;
            } else if nums[mid as usize] > target {
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        -1
    }
}