class CustomComparator implements Comparator<Pair<Integer, Integer>> {
    public int compare(Pair<Integer, Integer> a, Pair<Integer, Integer> b) {
        if (!a.getKey().equals(b.getKey())) {
            return Integer.compare(b.getKey(), a.getKey());
        }
        return Integer.compare(b.getValue(), a.getValue());
    }
}

class Solution {
    public int maximumSum(int[] nums) {
        int n = nums.length;
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(new CustomComparator());
        int count = 0;
        for(int i = 0; i < n; i++){
            int temp = nums[i];
            count = 0;
            while (temp > 0){
                count += (temp % 10);
                temp /= 10;
            }
            pq.add(new Pair(count, nums[i]));
        }
        Pair<Integer, Integer> pair1 = pq.remove();
        count = -1;
        while(!pq.isEmpty()){
            Pair<Integer, Integer> pair2 = pq.remove();
            if(pair1.getKey().equals(pair2.getKey())){
                if(pair1.getValue() + pair2.getValue() > count) count = pair1.getValue() + pair2.getValue();
            }
            pair1 = pair2;
        }
        return count;
    }
}