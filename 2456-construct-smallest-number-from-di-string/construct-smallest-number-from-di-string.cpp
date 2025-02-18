class Solution {
public:
    bool backtrack(int idx, string& result, string pattern, unordered_map<int, bool>& check, int size){
        if (idx == size) return true;
        else{
            for (int i = 1; i < 10; i++){
                if (check[i]) continue;
                else{
                    if (pattern[idx - 1] == 'I'){
                        if (i + '0' <= result[idx - 1]) continue;
                        else{
                            check[i] = true;
                            char temp = i + '0';
                            result += temp;
                            if (backtrack(idx + 1, result, pattern, check, size)) return true;
                            result.pop_back();
                            check[i] = false;
                        }
                    }
                    else{
                        if (i + '0' >= result[idx - 1]) continue;
                        else{
                            check[i] = true;
                            char temp = i + '0';
                            result += temp;
                            if (backtrack(idx + 1, result, pattern, check, size)) return true;
                            result.pop_back();
                            check[i] = false;
                        }
                    }
                }
            }
            return false;
        }
    }
    string smallestNumber(string pattern) {
        unordered_map<int, bool> check;
        int size = pattern.size() + 1;
        string result = "";
        int idx = 0;
        for (int i = 1; i < 10; i++){
            if (check[i]) continue;
            else{
                check[i] = true;
                char temp = i + '0';
                result += temp;
                if (backtrack(idx + 1, result, pattern, check, size)) return result;
                result.pop_back();
                check[i] = false;
            }
        }
        return result;
    }
};