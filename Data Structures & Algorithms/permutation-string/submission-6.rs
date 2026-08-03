use std::collections::HashMap;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut original = HashMap::new();
        for l in s1.as_bytes() {
            *original.entry(l).or_insert(0) += 1
        }
        let mut check = HashMap::new();
        let n = s2.len();

        let mut r = 0;
        let mut l = 0;

        let s2_bytes = s2.as_bytes();
        while r < n {
            *check.entry(&s2_bytes[r as usize]).or_insert(0) += 1;
            if r - l + 1 > s1.len() {
                *check.entry(&s2_bytes[l as usize]).or_insert(0) -= 1;
                if *check.entry(&s2_bytes[l as usize]).or_insert(0) == 0 {
                    check.remove(&s2_bytes[l as usize]);
                }
                l += 1
            }
            if original == check {
                return true;
            }
            r += 1
        }
        false
    }
}
