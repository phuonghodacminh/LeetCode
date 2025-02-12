/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    check = {}
    let n = nums.length
    let count = 0
    let temp = 0
    let result = -1
    for(let i = 0; i < n; i++){
        count = 0
        temp = nums[i]
        while(temp > 0){
            count += (temp % 10)
            temp = Math.floor(temp /= 10)
        }
        if (check[count] == undefined){
            check[count] = nums[i]
        }
        else {
            if (result < nums[i] + check[count]) result = nums[i] + check[count]
            if (nums[i] > check[count]) check[count] = nums[i]
        }
    }
    return result;
};