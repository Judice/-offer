# coding=utf-8
"""
对于一个有序循环数组arr，返回arr中的最小值。有序循环数组是指，有序数组左边任意长度的部分放到右边去，右边的部分拿到左边来。比如数组[1,2,3,3,4]，是有序循环数组，[4,1,2,3,3]也是。
给定数组arr及它的大小n，请返回最小值。
"""
class MinValue:
    def getMin(self, arr, n):
        left=0
        right=n-1
        if arr[left] <arr[right]:
            return arr[left]
        while left<right:  # 可以left=right 多执行一次while循环
            if (right-left)>1:
                mid=left+(right-left)/2
                if arr[left]>arr[mid]:
                    right=mid
                elif arr[mid]>arr[left]:
                    left=mid       # left必指向前段递增序列,不能写left=mid+1
                elif arr[mid]==arr[left] and arr[mid]==arr[right]:
                    right-=1
            else:
                res = arr[right]
                left+=1
        return res


class MinValue:
    def getMin(self, arr, n):
        left = 0
        right = n - 1
        if arr[0]<arr[n-1]:
            return arr[0]
        while left <= right:
            mid = left + (right - left)/2
            if arr[mid] < arr[left]:
                    right = mid
            elif arr[mid] > arr[right]:
                    left = mid +1
            else:
                cur = arr[left]
                left = left +1
                while left <= right:
                    if cur > arr[left]:
                        cur = arr[left]
                    left=left+1
                return cur