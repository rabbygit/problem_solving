/**
 * [Problem ref]{@link  https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/}
 * @description Given an integer array nums where the elements are sorted in ascending order, 
 * convert it to a height-balanced binary search tree.
 * A height-balanced binary tree is a binary tree in which 
 * the depth of the two subtrees of every node never differs by more than one.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

 function TreeNode(val, left, right) {
     this.val = (val===undefined ? 0 : val)
     this.left = (left===undefined ? null : left)
     this.right = (right===undefined ? null : right)
 }
 
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
const sortedArrayToBST = function (nums) {

    function constructBST(left, right) {
        if (left > right) {
            return null
        }

        let mid = parseInt((left + right) / 2)
        let root = new TreeNode(nums[mid])

        root.left = constructBST(left, mid - 1)
        root.right = constructBST(mid + 1, right)

        return root
    }

    return constructBST(0, nums.length - 1)
};