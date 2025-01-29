class Solution {
    int find(vector<int>& dsuf, int v){
        if(dsuf[v] == -1) return v;
        else return dsuf[v] = find(dsuf, dsuf[v]);
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> dsuf(edges.size() + 1, -1);
        for(int i = 0; i < edges.size(); i++){
            int xp = find(dsuf, edges[i][0]);
            int yp = find(dsuf, edges[i][1]);
            if(xp == yp) return edges[i];
            else dsuf[xp] = yp;
        }
        return {0, 0};
    }
};