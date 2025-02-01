class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int sum = nums1.size() + nums2.size();
        int mid = sum / 2;
        int l1 = 0;
        int l2 = 0;
        vector<int> nums;
        while (l1 < nums1.size() && l2 < nums2.size()){
            if(nums1[l1] < nums2[l2]){
                nums.push_back(nums1[l1]);
                l1++;
            }
            else{
                nums.push_back(nums2[l2]);
                l2++;
            }
        }
        if (l1 < nums1.size()){
            while (l1 < nums1.size()){
                nums.push_back(nums1[l1]);
                l1++;
            }
        }
        else{
            while (l2 < nums2.size()){
                nums.push_back(nums2[l2]);
                l2++;
            }
        }
        if (sum % 2) return nums[mid];
        else return 1.0*(nums[mid - 1] + nums[mid]) / 2.0;
    }
};