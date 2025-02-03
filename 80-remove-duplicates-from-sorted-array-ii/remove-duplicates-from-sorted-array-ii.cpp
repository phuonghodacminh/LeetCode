class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;
        int curr = -1;
        int c = 0;
        for(int i = 0; i < nums.size(); i++){
            if(curr != nums[i]){
                curr = nums[i];
                c = 1;
            }
            else{
                c++;
                if (c > 2){
                    nums.erase(nums.begin() + i);
                    i--;
                }
            }
        }
        return nums.size();
    }
};