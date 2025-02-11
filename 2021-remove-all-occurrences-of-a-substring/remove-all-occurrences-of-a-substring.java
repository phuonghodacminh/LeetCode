class Solution {
    public String removeOccurrences(String s, String part) {
        int p = part.length();
        int n = s.length();
        if(p > n) return s;
        else{
            Stack<Character> check = new Stack<>();
            String result = "";
            for(int i = 0; i < n; i++){
                result = "";
                check.push(s.charAt(i));
                if(check.size() >= p){
                    for(int j = 0; j < p; j++){
                        result = check.pop() + result;
                    }
                    if(!result.equals(part)){
                        for(int j = 0; j < p; j++){
                            check.push(result.charAt(j));
                        }
                    }
                }
            }
            result = "";
            while(!check.empty()){
                result = check.pop() + result;
            }
            return result;
        }
    }
}