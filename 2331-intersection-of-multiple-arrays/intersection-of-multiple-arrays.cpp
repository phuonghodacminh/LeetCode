class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        unordered_map<int, int> check;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < nums[i].size(); j++){
                check[nums[i][j]]++;
            }
        }
        vector<int> result;
        for (int i = 1; i < 1001; i++){
            if(check[i] == n) result.push_back(i);
        }
        return result;
    }
};