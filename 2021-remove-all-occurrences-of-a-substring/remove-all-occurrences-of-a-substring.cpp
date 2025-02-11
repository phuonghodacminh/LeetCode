class Solution {
public:
    string removeOccurrences(string s, string part) {
        int p = part.size();
        int n = s.size();
        if (p > n) return s;
        stack<char> check;
        string temp = "";
        for(int i = 0; i < n; i++){
            temp = "";
            check.push(s[i]);
            if(check.size() >= p){
                for(int j = 0; j < p; j++){
                    temp = check.top() + temp;
                    check.pop();
                }
                if(temp != part){
                    for(int j = 0; j < p; j++){
                        check.push(temp[j]);
                    }
                }
            }
        }
        temp = "";
        while(!check.empty()){
            temp = check.top() + temp;
            check.pop();
        }
        return temp;
    }
};