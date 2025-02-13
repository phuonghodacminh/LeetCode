/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    let minHeap = new MinPriorityQueue()
    var count = 0
    for (let num of nums){
        minHeap.enqueue(num)
    }
    var min1 = minHeap.front().element
    var min2 = -1
    while(min1 < k){
        minHeap.dequeue()
        min2 = minHeap.front().element
        minHeap.dequeue()
        minHeap.enqueue(Math.min(min1, min2) * 2 + Math.max(min1, min2))
        count++
        min1 = minHeap.front().element
    }
    return count
};