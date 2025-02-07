class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
       unordered_map<int, int> check;
       unordered_map<int, int> map;
       vector<int> result;
       int add = 0;
       for(int i = 0; i < queries.size(); i++){
            if(check[queries[i][1]] == 0 || (map[queries[i][0]] == queries[i][1] && check[queries[i][1]] == 1)) add++;
            if(map[queries[i][0]] == 0){
                check[queries[i][1]]++;
            }
            else{
                check[map[queries[i][0]]]--;
                if(check[map[queries[i][0]]] == 0) add--;
                check[queries[i][1]]++;
            }
            map[queries[i][0]] = queries[i][1];
            result.push_back(add);
       } 
       return result;
    }
};