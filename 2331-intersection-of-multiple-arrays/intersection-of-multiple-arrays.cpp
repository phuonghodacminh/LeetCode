class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        unordered_map<int, int> check;
        vector<int> result;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < nums[i].size(); j++){
                check[nums[i][j]]++;
                if(check[nums[i][j]] == n) result.push_back(nums[i][j]);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};