# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:36:33 2018

@author: wujiaqian
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        start = head
        if not head:
            return head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return start

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

s = Solution()
s.removeElements(node1,2)