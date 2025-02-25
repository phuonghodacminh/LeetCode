class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size();
        int countOdd = 0;
        int countEven = 1;
        int prefixSum = 0;
        long long count = 0;
        for (int i = 0; i < n; i++){
            prefixSum += arr[i];
            if (prefixSum % 2){
                count += countEven;
                countOdd ++;
            }
            else{
                count += countOdd;
                countEven ++;
            }
        }
        count %= 1000000007;
        return count;
    }
};