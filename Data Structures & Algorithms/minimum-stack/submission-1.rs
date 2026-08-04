struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>
}

impl MinStack {
    pub fn new() -> Self {
        Self {
            stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }

    pub fn push(&mut self, val: i32) {
        if self.stack.is_empty() && self.min_stack.is_empty() {
            self.stack.push(val);
            self.min_stack.push(val);
        } else {
            self.stack.push(val);
            let val = std::cmp::min(val, *self.min_stack.last().unwrap());
            self.min_stack.push(val);
        }
    }

    pub fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }

    pub fn top(&self) -> i32 {
       let a = *self.stack.last().unwrap();
       a
    }

    pub fn get_min(&self) -> i32 {
        let a = *self.min_stack.last().unwrap();
        a
    }
}
