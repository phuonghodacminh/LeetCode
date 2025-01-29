class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> check;
        for(int i=0;i<nums.size();i++){
            if(check.find(target-nums[i])==check.end()){
                check[nums[i]]=i;
            }
            else{
                return {check[target-nums[i]],i};
            }
        }
        return {};
    }
};