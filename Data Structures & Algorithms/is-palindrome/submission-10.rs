impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut new = String::new();
        for letter in s.chars() {
            if letter.is_alphanumeric() {
                new.push(letter);
            }
        }
        let mut i = 0;
        let mut j = new.len() - 1;
        let new = new.to_lowercase();
        if new.len() <= 1  {
            return true;
        }

        while i <= j {
            if new.as_bytes()[i as usize] == new.as_bytes()[j as usize] {
                i += 1;
                j -= 1;
            } else {
                return false
            }
        }

        true
    }
}
