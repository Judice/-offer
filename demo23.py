# coding=utf-8
"""
有一个有序数组arr，其中不含有重复元素，请找到满足arr[i]==i条件的最左的位置。如果所有位置上的数都不满足条件，返回-1。
给定有序数组arr及它的大小n，请返回所求值。
"""
class Find:
    def findPos(self, arr, n):
        if n == 0 or arr[0] > 0 or arr[n - 1] < n - 1:
            return -1
        left = 0
        right = n - 1
        res = -1
        while left <= right:
            mid = left+(right-left) / 2
            if arr[mid] == mid:
                res = mid
                right = mid-1
            elif arr[mid]>mid:
                right = mid
            else:
                left = mid+1
        return res