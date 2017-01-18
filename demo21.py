# coding=utf-8
"""
对于一个有序数组arr，再给定一个整数num，请在arr中找到num这个数出现的最左边的位置。
给定一个数组arr及它的大小n，同时给定num。请返回所求位置。若该元素在数组中未出现，请返回-1。
"""

class LeftMostAppearance:
    def findPos(self, arr, n, num):
        left = 0
        right = n
        res = -1
        while left< right:
            mid = left +(right-left)/2
            if arr[mid] == num:
                res = mid
                right = mid
            elif arr[left]<= num < arr[mid]:
                right = mid
            else:
                left = mid+1
        return res

class LeftMostAppearance:
    def findPos(self, arr, n, num):
        # write code here
        left = 0
        right = n-1
        while left<=right:
            mid = left+(right-left)/2
            if arr[mid] == num:
                while arr[mid] == num:
                    mid -= 1
                return mid+1
            elif arr[mid]>num:
                right = mid-1
            else:
                left = mid+1
        return -1

class LeftMostAppearance:
    def findPos(self, arr, n, num):
        left = 0
        right = n-1
        res = 0
        while left<= right:
            mid = left +(right-left)/2
            if arr[mid] == num:
                res = mid
                right = mid-1
            elif arr[left]<= num < arr[mid]:
                right = mid
            else:
                left = mid+1
        return res
