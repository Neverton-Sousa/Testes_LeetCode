# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        current = head
        newHead = dummy = ListNode(0)
        number = 0

        while current:
            number = number * 10 + current.val
            current = current.next

        number *= 2

        if number == 0:
            return ListNode(0)

        numbers = []

        while number > 0:
            digit = number % 10
            number = number // 10
            numbers.append(digit)

        for num in reversed(numbers):
            dummy.next = ListNode(num)
            dummy = dummy.next

        return newHead.next


#     2816. Double a Number Represented as a Linked List
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.


# Example 1:


# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
# Example 2:


# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.
