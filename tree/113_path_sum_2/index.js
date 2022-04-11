/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
const pathSum = function (root, targetSum) {
    const result = []

    function possiblePath(root, sum, sub_result) {
        if (!root) return

        sum += root.val
        sub_result.push(root.val)
        
        possiblePath(root.left, sum, sub_result)
        
        // check if it is leaf node and 
        // targetSum is equal to the sum upto this node
        if (!root.left && !root.right && targetSum === sum) {
            result.push([...sub_result])
        }

        possiblePath(root.right, sum, sub_result)

        sub_result.pop()
    }

    possiblePath(root, 0, [])

    return result
};