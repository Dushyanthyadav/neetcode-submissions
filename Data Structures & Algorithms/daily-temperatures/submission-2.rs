impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::new();
        let mut index = Vec::new();

        let mut output: Vec<i32> = vec![0; temperatures.len()];

        for i in 0..temperatures.len() {
            while !stack.is_empty() && *stack.last().unwrap() < temperatures[i] {
                let nex = i - index.last().unwrap();
                output[index.pop().unwrap()] = nex as i32;
                stack.pop().unwrap();
            }
            stack.push(temperatures[i]);
            index.push(i);
        }

        output


    }
}