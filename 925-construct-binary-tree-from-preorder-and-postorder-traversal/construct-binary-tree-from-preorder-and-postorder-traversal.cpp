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
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        if (preorder.empty()) return nullptr;
        TreeNode* newNode = new TreeNode(preorder[0]);
        if (preorder.size() == 1) return newNode;
        preorder.erase(preorder.begin());
        postorder.pop_back();
        int left_tree_size = find(postorder.begin(), postorder.end(), preorder[0]) - postorder.begin() + 1;
        vector<int> pre_left(preorder.begin(), preorder.begin() + left_tree_size);
        vector<int> pre_right(preorder.begin() + left_tree_size, preorder.end());
        vector<int> post_left(postorder.begin(), postorder.begin() + left_tree_size);
        vector<int> post_right(postorder.begin() + left_tree_size, postorder.end());
        newNode->left = constructFromPrePost(pre_left, post_left);
        newNode->right = constructFromPrePost(pre_right, post_right);
        return newNode;
    }
};