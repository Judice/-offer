# coding=utf-8
"""
  题目描述:
         某把一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转，
         输入一个递增排序的数组的一个旋转，例如数组{3, 4, 5, 1, 2} 为{1, 2, 3, 4, 5} 的一个旋转
         先从数组中查找某个数,并输出相应的索引位置,若不存在输出-1
"""
class Solution():
    def search(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left)/2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid
        return -1

if __name__ == "__main__":
    nums = [8,9,1,2,3,4,5,6,7]
    s = Solution()
    print s.search(nums,8)