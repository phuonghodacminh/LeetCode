class Solution {
public:
    vector<int> divisor(int k){
        int t = sqrt(k);
        vector <int> result;
        for (int i = 1; i <= t; i++){
            if(k % i == 0){
                int r = k / i;
                if (r == i) result.push_back(i);
                else{
                    result.push_back(i);
                    result.push_back(r);
                }
            }
            else;
        }
        return result;
    }
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        int g = groups.size();
        int e = elements.size();
        unordered_map<int, bool> check1;
        unordered_map<int, int> check2;
        for(int i = 0; i < e; i++){
            if(check1[elements[i]]);
            else{
                check1[elements[i]] = true;
                check2[elements[i]] = i;
            }
        }
        vector<int> result;
        int temp;
        for(int i = 0; i < g; i++){
            temp = -1;
            vector<int> divis = divisor(groups[i]);
            int d = divis.size();
            for(int j = 0; j < d; j++){
                if(!check1[divis[j]]);
                else{
                    if(check2[divis[j]] < temp || temp == -1) temp = check2[divis[j]];
                    else;
                }
            }
            result.push_back(temp);
        }
        return result;
    }
};