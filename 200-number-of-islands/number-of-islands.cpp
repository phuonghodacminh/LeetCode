class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        queue<int> q1;
        queue<int> q2;
        unordered_map<int, bool> visited;
        int x_dir[] = {0, 0, 1, -1};
        int y_dir[] = {1, -1, 0, 0};
        int dir = 0;
        int count = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == '1') q1.push(i * grid[0].size() + j);
            }
        }
        while(!q1.empty()){
            int temp = q1.front();
            q1.pop();
            if(visited[temp]);
            else{
                q2.push(temp);
                visited[temp] = true;
                while(!q2.empty()){
                    int temp2 = q2.front();
                    q2.pop();
                    int x = temp2 / grid[0].size();
                    int y = temp2 % grid[0].size();
                    while(dir < 4){
                        int new_x = x + x_dir[dir];
                        int new_y = y + y_dir[dir];
                        int temp3 = new_x * grid[0].size() + new_y;
                        if(new_x >= 0 && new_x < grid.size() && new_y >= 0 && new_y < grid[0].size() && !visited[temp3] && grid[new_x][new_y] == '1'){
                            visited[temp3] = true;
                            q2.push(temp3);
                        }
                        dir++;
                    }
                    dir = 0;
                }
                count++;
            }
        }
        return count;
    }
};