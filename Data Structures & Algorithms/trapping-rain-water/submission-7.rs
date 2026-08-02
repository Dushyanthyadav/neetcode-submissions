impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();

        if n == 0 { return 0; }

        let mut res = 0;

        for i in 0..n {
            let mut left = height[i];
            let mut right = height[i];

            for j in 0..i {
                left = std::cmp::max(height[j], left);
            }

            for j in i+1..n {
                right = std::cmp::max(height[j], right);
            }

            res += std::cmp::min(left,right)-height[i];
        }
        res
    }
}
