class Solution {
public:
    bool backtrack(int i, vector<int>& check, int n, unordered_map<int, bool>& seen){
        bool v = true;
        for (int m = 1; m <= n; m++){
            if (!seen[m]) v = false;
        }
        if (v || i >= 2 * n - 1) return true;
        if (check[i] != -1) return backtrack(i + 1, check, n, seen);
        for(int j = n; j > 0; j--){
            if (seen[j]) continue;
            if (i + j >= 2 * n - 1 && j != 1) continue;
            if (j != 1 && check[i + j] != -1) continue;
            check[i] = j;
            if (j != 1) check[i + j] = j;
            seen[j] = true;
            if (backtrack(i + 1, check, n, seen)) return true;
            else if (j != 1) check[i + j] = -1;
            seen[j] = false;
            check[i] = -1;
        }
        return false;
    }
    vector<int> constructDistancedSequence(int n) {
        vector<int> check(2 * n - 1, -1);
        unordered_map<int, bool> seen;
        backtrack(0, check, n, seen);
        return check;
    }
};