# coding=utf-8
"""
题目描述
      输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:

    def Merge(self, pHead1, pHead2):
        # write code here
        result = None
        current = None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        while pHead1 and pHead2:
           if pHead1.val <= pHead2.val:
              if result == None:            # 取较小值作为头结点
                  result = current = pHead1 # current为合并后的链表工作指针
              else:
                  current.next = pHead1     # 取较小值加入合并后的链表
                  current = current.next    # 工作指针后移一位
              pHead1 = pHead1.next          # 链表1后移一位
           else:
               if result == None:
                   result = current = pHead2
               else:
                   current.next = pHead2
                   current = current.next
               pHead2 = pHead2.next
        if pHead1:                         # 链表2遍历完
            current.next = pHead1          # 工作指针指向链表1
        if pHead2:
            current.next = pHead2
        return result