impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();

        for i in tokens {
            match i.parse::<i32>() {
                Ok(num) => stack.push(num),
                Err(_) => {
                    let second = stack.pop().unwrap();
                    let first = stack.pop().unwrap();
                    match i.as_str(){
                        "+" => stack.push(first + second),
                        "-" => stack.push(first - second),
                        "*" => stack.push(first * second),
                        "/" => stack.push(first / second),
                        _ => unreachable!()
                    }
                }
            }
        }
        stack.pop().unwrap()
    }
}
