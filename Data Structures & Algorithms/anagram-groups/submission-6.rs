use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut a: HashMap<[u8; 26], Vec<String>> = HashMap::new();

        for word in strs{
            let mut count = [0u8; 26];

            for letter in word.bytes() {
                count[(letter - b'a') as usize] += 1;
            }

            a.entry(count).or_default().push(word)
        
        }
        a.into_values().collect()
    }
}
