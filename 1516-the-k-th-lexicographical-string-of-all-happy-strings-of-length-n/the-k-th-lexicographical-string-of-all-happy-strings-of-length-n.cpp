class Solution {
public:
    bool backtracking(string& result, int idx, int& count, int n, int k){
        if (idx == n) {
            count++;
            if (count == k) return true;
            else return false;
        }
        for (int i = 0; i < 3; i++){
            char temp = i + 'a';
            if (idx == 0) result += temp;
            else{
                if (temp == result[result.size() - 1]) continue;
                else result += temp;
            }
            cout << idx << " " << result << " " << count << endl;
            if (backtracking(result, idx + 1, count, n, k)) return true;
            result.pop_back();
        }
        return false;
    }
    string getHappyString(int n, int k) {
        string result = "";
        int count = 0;
        if (backtracking(result, 0, count, n, k)) return result;
        else return "";
    }
};