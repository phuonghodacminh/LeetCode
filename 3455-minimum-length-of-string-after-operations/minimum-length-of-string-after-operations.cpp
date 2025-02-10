class Solution {
public:
    int minimumLength(string s) {
        vector<int> freq(26, 0);
        int n = s.size();
        for(int i = 0; i < n; i++){
            freq[s[i] - 'a']++;
        }
        int min = 0;
        for(int i = 0; i < 26; i++){
            if(freq[i] == 0);
            else if(freq[i] % 2) min++;
            else min += 2;
        }
        return min;
    }
};