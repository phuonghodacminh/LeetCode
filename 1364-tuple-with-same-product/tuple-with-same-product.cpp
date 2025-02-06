class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map <int, int> check;
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++){
                check[nums[i] * nums[j]]++;
            }
        }
        for(auto i = check.begin(); i != check.end(); i++){
            int save = i -> second;
            if (save == 0 || save == 1);
            else{
                result += save * (save - 1) * 4;
            }
        }
        return result;
    }
};