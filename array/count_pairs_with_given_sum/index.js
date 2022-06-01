/**
 * @description Given an array of N integers, and an integer K, 
 * find the number of pairs of elements in the array whose sum is equal to K.
 * @param {number[]} arr
 * @param {number} n
 * @param {number} k
 * @return {number}
*/
function getPairsCount(arr,n,k){
    const sum_map = {}
    let result = 0

    for (let index = 0; index < n; index++) {
        const sub = k - arr[index]

        if (sum_map[sub] !== undefined) {
            result += sum_map[sub]
            sum_map[sub]++
        }else{
            sum_map[arr[index]] = 1
        }
    }

    return result
}