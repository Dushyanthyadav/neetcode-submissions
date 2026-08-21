/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int goodNodes(TreeNode* root) {

        int count = 0;

        good(root, root->val, &count);

        return count;
        
    }

    void good(TreeNode* node, int max, int *count) {
        if (node == nullptr) {
            return;
        }

        if (node->val >= max) {
            *count += 1;
            max = node->val;
        }

        good(node->left, max, count);
        good(node->right, max, count);
    }
};