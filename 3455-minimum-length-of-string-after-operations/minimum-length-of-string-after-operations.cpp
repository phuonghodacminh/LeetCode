class Solution {
public:
    int minimumLength(string s) {
        unordered_map<char, int> freq;
        int n = s.size();
        for(int i = 0; i < n; i++){
            freq[s[i]]++;
        }
        int min = 0;
        for(auto it = freq.begin(); it != freq.end(); it++){
            int c = it -> second;
            if(c % 2) min++;
            else min += 2;
        }
        return min;
    }
};