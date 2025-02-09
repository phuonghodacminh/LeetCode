class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int, int> check;
        long long n = nums.size();
        long long all = n * (n - 1) / 2;
        for(int i = 0; i < n; i++){
            nums[i] -= i;
            check[nums[i]]++;
        }
        for(auto it = check.begin(); it != check.end(); it++){
            long long temp = it -> second;
            temp = (temp * (temp - 1)) / 2;
            all -= temp;
        }
        return all;
    }
};