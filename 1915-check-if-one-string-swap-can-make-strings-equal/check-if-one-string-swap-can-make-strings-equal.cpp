class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int count = 0;
        bool check = false;
        int temp = -1;
        for(int i = 0; i < s1.size(); i++){
            if (s1[i] != s2[i]){
                if (count == 0){
                    temp = i;
                    count++;
                }
                else if (count == 1){
                    if (s1[i] == s2[temp] && s2[i] == s1[temp]){
                        check = true;
                        count++;
                    }
                    else return false;
                }
                else return false;
            }
        }
        if (count == 0) return true;
        return check;
    }
};