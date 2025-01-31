class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxLeft = 0;
        int maxRight = 0;
        int sum = 0;
        while(left < right){
            if(height[left] < height[right]){
                if(height[left] < maxLeft){
                    sum += (maxLeft - height[left]);
                }
                else{
                    maxLeft = height[left];
                }
                left++;
            }
            else{
                if(height[right] < maxRight){
                    sum += (maxRight - height[right]);
                }
                else{
                    maxRight = height[right];
                }
                right--;
            }
        }
        return sum;
    }
};