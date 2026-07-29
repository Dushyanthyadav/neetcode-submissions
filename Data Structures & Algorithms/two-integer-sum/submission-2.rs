use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash = HashMap::new();
        let mut first: i32 = 0;
        let mut second: i32 = 0;
        for i in 0..nums.len() {
            let b = target - nums[i];
            if hash.contains_key(&nums[i]) {
                first = hash[&nums[i]];
                second = i as i32;
                break;
            }
            hash.insert(b, i as i32);
        }

        if first > second {
            return vec![second, first];
        } else {
            return vec![first, second];
        }
    }
}
