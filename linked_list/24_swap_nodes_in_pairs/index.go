package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	// return if list has one or no node
	if head == nil || head.Next == nil {
		return head
	}

	// two pointer; one is ahead of another
	slow := head
	fast := head.Next
	var prev *ListNode = nil

	for slow != nil && fast != nil {
		temp := fast.Next

		// swap head nodes
		if prev == nil {
			head = fast
			head.Next = slow
			head.Next.Next = temp
		} else {
			// swap nodes from middle
			prev.Next = fast
			prev.Next.Next = slow
			slow.Next = temp
		}

		// keep track of previous node for swaping from the middle of the list
		prev = slow

		// update the pointers to next
		slow = temp
		if slow != nil {
			fast = slow.Next
		}
	}

	return head
}
