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
            j = i +1                    # 创建第二个指针
            if i == stop:               # if语句用于添加最后一个元素
                new_list.append(nums[i])
                break                  # 跳出while循环
            else:
                if nums[i] == nums[j]:
                    while j <= stop and  nums[i] == nums[j]:
                        j += 1
                new_list.append(nums[i])
                i = j                     # 传递指针
        return new_list

if __name__ == "__main__":
    List = [1,1,2,3,4,4,4,5,5,6,7,8,8,9,9]
    s = Solution()
    print s.remove(List)
