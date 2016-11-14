# coding=utf-8
"""
   题目描述:
          去除列表中的重复元素
"""
class Solution():
    def remove(self, nums):
        i = 0
        new_list=[]
        stop = len(nums)-1
        while i <= stop:
            j = i +1
            if i == stop:
                new_list.append(nums[i])
                i += 1
            else:
                if nums[i] == nums[j]:
                    while j <= stop and  nums[i] == nums[j]:
                        j += 1
                new_list.append(nums[i])
                i = j
        return new_list

if __name__ == "__main__":
    List = [1,1,2,3,4,4,4,5,5,6,7,8,8,9,9]
    s = Solution()
    print s.remove(List)
