/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/number-of-provinces/}
 * @description There are n cities. Some of them are connected, while some are not. 
 * If city a is connected directly with city b, and city b is connected directly with city c,
 * then city a is connected indirectly with city c.
 * A province is a group of directly or indirectly connected cities and no other cities outside of the group.
 */

class UnionFind{
    constructor(size){
        this.root = [...Array(size).keys()] // fill with index with default value same as index
        this.rank = Array(size).fill(1) // fill all index with default value to 1
        this.provinces = size
    }

    find(x){
        if (x === this.root[x]) {
            return x 
        }
        this.root[x] = this.find(this.root[x])
        return this.root[x]
    }

    union(x,y){
        let rootX = this.find(x)
        let rootY = this.find(y)

        if (rootX !== rootY) {
            if (this.rank[rootX] > this.rank[rootY]) {
                this.root[rootY] = rootX
            } else if(this.rank[rootX] < this.rank[rootY]){
                this.root[rootX] = rootY
            }else{
                this.root[rootY] = rootX
                this.rank[rootX]++
            }

            this.provinces--
        }
    }

    total_provinces(){
        return this.provinces
    }
}


/**
 * @param {number[][]} isConnected
 * @return {number}
 */
const findCircleNum = function(isConnected) {
    const n = isConnected.length
    const uf = new UnionFind(n)

    for (let row = 0; row < n; row++) {
        for (let column = row+1; column < n; column++) {
            if (isConnected[row][column]) {
                uf.union(row,column)
            }
        }
    }

    return uf.total_provinces()
};