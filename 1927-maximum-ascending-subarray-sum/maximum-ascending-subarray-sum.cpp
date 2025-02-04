class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int result = 0;
        int temp = nums[0];
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] > nums[i - 1]) temp += nums[i];
            else{
                if (temp > result) result = temp;
                temp = nums[i];
            }
        }
        if (temp > result) return temp;
        else return result;
    }
};