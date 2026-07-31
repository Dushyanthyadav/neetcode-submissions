use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = vec![HashSet::new();9];
        let mut cols = vec![HashSet::new();9];
        let mut boxs = vec![HashSet::new();9];

        for r in 0..9 {
            for c in 0..9 {
                let val = board[r][c];
                if val == '.' {
                    continue;
                }

                // let val: i32 = val.parse().unwrap();
                let box_index = (r/3)*3 + (c/3);

                if rows[r as usize].contains(&val) || cols[c as usize].contains(&val) || boxs[box_index as usize].contains(&val) {
                    return false
                }

                rows[r].insert(val);
                cols[c].insert(val);
                boxs[box_index].insert(val);
            }
        }
        true
    }
}
