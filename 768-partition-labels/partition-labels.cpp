class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> check;
        unordered_set<char> seen;
        vector<int> result;
        bool c = true;
        int n = s.size();
        int sum = 0;
        for (int i = 0; i < n; i++){
            check[s[i]]++;
        }
        for (int i = 0; i < n; i++){
            seen.insert(s[i]);
            check[s[i]]--;
            c = true;
            for (char x : seen){
                if (check[x]){
                    c = false;
                    break;
                }
            }
            if (c){
                if (!result.size()){
                    result.push_back(i + 1);
                    sum += (i + 1);
                }
                else{
                    result.push_back(i - sum + 1);
                    sum += (i - sum + 1);
                }
                seen.clear();
            }
        }
        return result;
    }
};