impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut largest = 0;

        let mut i = 0;
        let mut j = heights.len() - 1;

        while i < j {
            let small = std::cmp::min(heights[i], heights[j]);
            let cap = small*((j-i) as i32);
            if small == heights[i] {
                i += 1;
            } else {
                j -= 1;
            }
            if cap > largest {
                largest = cap;
            }
        }
        largest
    }
}
