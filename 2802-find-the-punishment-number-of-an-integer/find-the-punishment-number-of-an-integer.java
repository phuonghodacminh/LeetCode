class Solution {
    public int punishmentNumber(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++){
            int square = i * i;
            String s = Integer.toString(square);
            if(backtrack(s, 0, 0, i)){
                count += square;
            }
        }
        return count;
    }
    public boolean backtrack(String s, int idx, int current_sum, int i){
        int k = s.length();
        if (idx == k){
            if (current_sum == i) return true;
            else return false;
        }
        for (int l = 1; l <= k - idx; l++){
            String temp = s.substring(idx, idx + l);
            int temp2 = Integer.parseInt(temp);
            if(backtrack(s, idx + l, current_sum + temp2, i)) return true;
        }
        return false;
    }
}