class Solution {
public:
    string clearDigits(string s) {
        stack<char> check;
        int x = s.size();
        for(int i = 0; i < x; i++){
            if(s[i] < '0' || s[i] > '9') check.push(s[i]);
            else check.pop();
        }
        string result = "";
        while(!check.empty()){
            result = check.top() + result;
            check.pop();
        }
        return result;
    }
};