class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> tree(n);
        for (int i = 0; i < n - 1; i++){
            tree[edges[i][0]].push_back(edges[i][1]);
            tree[edges[i][1]].push_back(edges[i][0]);
        }
        vector<int> bob_time(n, -1);
            function<bool(int, int, int, vector<vector<int>>&, vector<int>&)> dfs = [&](int src, int prev, int time,vector<vector<int>>& tree, vector<int>& bob_time) -> bool{
            if (src == 0){
                bob_time[src] = time;
                return true;
            }
            else{
                for (int i = 0; i < tree[src].size(); i++){
                    if (tree[src][i] == prev) continue;
                    else{
                        if (dfs(tree[src][i], src, time + 1, tree, bob_time)){
                            bob_time[src] = time;
                            return true;
                        }
                    }
                }
                return false;
            }
        };
        dfs(bob, -1, 0, tree, bob_time);
        deque<tuple<int, int, int, int>> dq;
        tuple<int, int, int, int> temp = make_tuple(0, 0, -1, amount[0]);
        dq.push_back(temp);
        int result = INT_MIN;
        while(!dq.empty()){
            temp = dq.front();
            dq.pop_front();
            int node = get<0>(temp);
            int time = get<1>(temp);
            int parent = get<2>(temp);
            int profit = get<3>(temp);
            for (int i = 0; i < tree[node].size(); i++){
                if(tree[node][i] == parent) continue;
                else{
                    int temp_profit = amount[tree[node][i]];
                    int temp_time = time + 1;
                    if(bob_time[tree[node][i]] != -1){
                        if (temp_time > bob_time[tree[node][i]]) temp_profit = 0;
                        else if (temp_time == bob_time[tree[node][i]]) temp_profit /= 2;
                    }
                    dq.push_back(make_tuple(tree[node][i], temp_time, node, profit + temp_profit));
                    if(tree[tree[node][i]].size() == 1){
                        if (profit + temp_profit > result) result = profit + temp_profit;
                    }
                }
            }
        }
        return result;
    }
};