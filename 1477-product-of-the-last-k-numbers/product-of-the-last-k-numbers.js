
var ProductOfNumbers = function() {
    this.products = [1]
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if (num === 0){
        this.products = [1]
    }
    else{
        this.products.push(num * this.products[this.products.length - 1]) 
    }
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    let n = this.products.length - 1
    let div = n - k
    if (div < 0) return 0
    return Math.round(this.products[n] / this.products[div])
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */