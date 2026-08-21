// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, max_val: i32) -> i32 {
            match node {
                None => 0,
                Some(n) => {
                    let n = n.borrow();
                    let res = if n.val >= max_val { 1 } else { 0 };
                    let new_max = max_val.max(n.val);
                    res + dfs(&n.left, new_max) + dfs(&n.right, new_max)
                }
            }
        }
        dfs(&root, i32::MIN)
    }
}
