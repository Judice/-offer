# coding=utf-8
"""
  题目描述:
         某一数组,其中的元素由小到大排列,现在数组在某个位置"截断" ,颠倒重新组合为一个新数组,
         现查找某个数值,并输出相应索引值,若不存在输出-1
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