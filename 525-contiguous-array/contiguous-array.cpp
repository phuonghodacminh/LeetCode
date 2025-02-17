class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++){
            if (!i){
                if (!nums[i]) nums[i] = -1;
                else nums[i] = 1;
            }
            else{
                if (!nums[i]) nums[i] = nums[i - 1] - 1;
                else nums[i] = nums[i - 1] + 1;
            }
        }
        unordered_map<int, int> check;
        int result = 0;
        for (int i = n - 1; i > -1; i--){
            if(!nums[i]){
                if (!result) result = i + 1;
            }
            else if(!check[nums[i]]) check[nums[i]] = i;
        }
        for (int i = 0; i < n; i++){
            check[nums[i]] -= i;
            if (check[nums[i]] > result) result = check[nums[i]];
        }
        return result;
    }
};