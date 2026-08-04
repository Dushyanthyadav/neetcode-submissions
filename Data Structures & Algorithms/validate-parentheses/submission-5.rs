use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() == 1 {
            return false;
        }

        let s_bytes = s.as_bytes();
        let mut stack = Vec::new();
        let mut hash = HashMap::from([
            (b')', b'('),
            (b']', b'['),
            (b'}', b'{')
        ]);

        for byte in s_bytes {
            if hash.contains_key(byte) && stack.len() == 0 {
                return false;
            } else {
                if hash.contains_key(byte) {
                    if hash.entry(*byte).or_default() != stack.last().unwrap() {
                        return false;
                    }
                    stack.pop();
                } else {
                    stack.push(*byte);
                }
            }
        }
        if stack.is_empty() {
            return true;
        } else {
            return false;
        }
    }
}
