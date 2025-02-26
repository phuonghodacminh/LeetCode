class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int currMax = nums[0];
        int currMin = nums[0];
        int max = nums[0];
        int min = nums[0];
        int n = nums.size();
        for (int i = 1; i < n; i++){
            if(currMax < 0) currMax = nums[i];
            else currMax += nums[i];
            if(max < currMax) max = currMax;
            if(currMin > 0) currMin = nums[i];
            else currMin += nums[i];
            if(min > currMin) min = currMin;
        }
        max = abs(max);
        min = abs(min);
        if (max > min) return max;
        return min;
    }
};