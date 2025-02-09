class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int x = n - 2;
        while(x >= 0){
            vector<int> needSort;
            for (int i = 0; i < n - x; i++){
                needSort.push_back(grid[i + x][i]);
            }
            sort(needSort.begin(), needSort.end(), greater<int>());
            for (int i = 0; i < n - x; i++){
                grid[i + x][i] = needSort[i];
            }
            x--;
        }
        x = 1;
        while(x < n){
            vector<int> needSort;
            for (int i = 0; i < n - x; i++){
                needSort.push_back(grid[i][i + x]);
            }
            sort(needSort.begin(), needSort.end());
            for (int i = 0; i < n - x; i++){
                grid[i][i + x] = needSort[i];
            }
            x++;
        }
        return grid;
    }
};