class Solution {
public:
    int backtrack(unordered_map<char, int>& check, vector<char> seen){
        int count = 0;
        for(int i = 0; i < seen.size(); i++){
            if (check[seen[i]]){
                check[seen[i]]--;
                count += 1 + backtrack(check, seen);
                check[seen[i]]++;
            }
        }
        return count;
    }
    int numTilePossibilities(string tiles) {
        unordered_map<char, int> check;
        vector<char> seen;
        int count = 0;
        int n = tiles.size();
        for (int i = 0; i < n; i++){
            if(check[tiles[i]] == 0) seen.push_back(tiles[i]);
            check[tiles[i]]++;
        }
        return backtrack(check, seen);
    }
};