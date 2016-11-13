# coding=utf-8
"""
   题目描述:
          把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
          输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
          例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
"""
class Solution():
    def search(self,nums):
        left = 0
        right = len(nums)-1
        while left < right:

            mid = left+(right-left)/2
            if nums[left] == nums[right] and nums[mid] == nums[right]:
                min_value = nums[left]
                for i in range(left+1, right):
                    if min_value > nums[i]:
                        min_value = nums[i]
                return min_value

            elif nums[mid] <= nums[left]:
                right = mid

            else:
                left = mid + 1
        return nums[right]

if __name__ == "__main__":
    s = Solution()
    nums01 = [1,0,1,1,1]
    print s.search(nums01)
    nums02 = [3,4,5,6,7,8,9,1,2]
    print s.search(nums02)

#或者开挂
    def search(self,RotateArray):
         return min(RotateArray)

