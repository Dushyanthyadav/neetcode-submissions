impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut lowest = prices[0];

        for price in prices {
            if price <= lowest {lowest = price;}
            let new_profit = price - lowest;
            if new_profit > profit {profit = new_profit;}
        }
        profit
    }
}
