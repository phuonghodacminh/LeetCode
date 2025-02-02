class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 1;
        while (i > 0 && nums[i] <= nums[i - 1]){
            i--;
        }
        if (i == 0) reverse(nums.begin(), nums.end());
        else{
            int temp = 101;
            int index = -1;
            for (int j = i; j < nums.size(); j++){
                if(nums[j] < temp && nums[j] > nums[i - 1]){
                    temp = nums[j];
                    index = j;
                }
            }
            swap(nums[index], nums[i - 1]);
            sort(nums.begin() + i, nums.end());
        }
    }
};