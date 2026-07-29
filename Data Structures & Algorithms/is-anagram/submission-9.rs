impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }

        let mut h1 = HashMap::with_capacity(s.len());
        let mut h2 = HashMap::with_capacity(s.len());

        for (c1, c2) in s.chars().zip(t.chars()) {
            *h1.entry(c1).or_insert(0) += 1;
            *h2.entry(c2).or_insert(0) += 1;
        }

        h1 == h2
    }
}
