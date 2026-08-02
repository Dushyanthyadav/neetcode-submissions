impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut lowest = prices[0];

        for price in prices {
            lowest = std::cmp::min(price, lowest);
            let new_profit = price - lowest;
            profit = std::cmp::max(new_profit, profit);
        }
        profit
    }
}
