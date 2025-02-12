/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    var l = 0
    var r = 46341
    var mid = -1
    var midsquare = -1
    while(l < r - 1){
        mid = Math.floor((l + r) / 2)
        midsquare = mid * mid
        if(midsquare < num) l = mid
        else if(midsquare > num) r = mid
        else return true
    }
    if (l * l === num || r * r === num) return true
    return false
};