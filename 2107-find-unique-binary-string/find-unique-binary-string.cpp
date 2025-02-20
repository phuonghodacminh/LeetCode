class Solution {
public:
    bool backtrack(int idx, string& result, int length, unordered_map<string, bool> check){
        if (idx == length){
            if (!check[result]) return true;
            else return false;
        }
        for (int i = 0; i < 2; i++){
            char temp = i + '0';
            result += temp;
            if (backtrack(idx + 1, result, length, check)) return true;
            result.pop_back();
        }
        return false;
    }
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_map<string, bool> check;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            check[nums[i]] = true;
        }
        string result = "";
        backtrack(0, result, n, check);
        return result;
    }
};