class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int result = 0;
        int left = 0;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i - 1] < nums[i]);
            else{
                if(result < i - left) result = i - left;
                left = i;
            }
        }
        if(result < nums.size() - left) result = nums.size() - left;
        left = 0;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i - 1] > nums[i]);
            else{
                if(result < i - left) result = i - left;
                left = i;
            }
        }
        if(result < nums.size() - left) result = nums.size() - left;
        return result;
    }
};