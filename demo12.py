# coding=utf-8
"""
   输入一个链表，从尾到头打印链表每个节点的值。
"""
class ListNode:
   def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)   #insert函数需要输入索引
            head = head.next
        return l
