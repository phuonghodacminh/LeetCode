class Solution {
public:
    TreeNode* recoverFromPreorder(string traversal) {
        int i = 0;
        return dfs(traversal, i, 0);
    }
    
    TreeNode* dfs(const string& traversal, int& idx, int depth) {
        int count = 0;

        while (idx < traversal.size() && traversal[idx] == '-') {
            count++;
            idx++;
        }

        if (count != depth) {
            idx -= count;
            return nullptr;
        }
        string s = "";
        while (idx < traversal.size() && isdigit(traversal[idx])) {
            s += traversal[idx++];
        }
        
        TreeNode* node = new TreeNode(stoi(s));
        
        node->left = dfs(traversal, idx, depth + 1);
        node->right = dfs(traversal, idx, depth + 1);

        return node;
    }
};
