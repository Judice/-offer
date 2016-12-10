# coding=utf-8
"""
题目描述
       输入一个链表，输出该链表中倒数第k个结点。
"""
class Node:
    def __init__(self):
        self.value = None
        self.next = None


class Solution:
    def FindKthToTail(self, head,k):
        list = []
        while head:
            list.append(head.value)
            head = head.next
        if k > len(list) or k < 1:
            return None
        return list[-k]

class Solution:
    def FindKthToTail(self, head, k):
        front = later = head     # 创建两个个指针
        for i in range(k):
            if front == None:
                return
            front = front.next
        while front != None:
            front = front.next
            later = later.next
        return later

