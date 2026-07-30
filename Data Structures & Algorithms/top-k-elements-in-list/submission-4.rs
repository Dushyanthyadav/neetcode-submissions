use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for num in &nums {
            *map.entry(*num).or_insert(0) += 1;
        }

        let mut vector = vec![vec![]; nums.len()+1];
        
        for (num, freq) in map {
            vector[freq as usize].push(num);
        }

        let mut result = Vec::new();

        for i in (0..vector.len()).rev() {
            for num in &vector[i] {
                result.push(*num);
                if result.len() == k as usize {
                    return result;
                }
            }
        }
        result
    }
}
