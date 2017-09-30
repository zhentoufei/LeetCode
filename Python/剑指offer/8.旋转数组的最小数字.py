# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 10:43'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '8.旋转数组的最小数字.py'

'''
二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。如果中间点大于首元素，
说明最小数字在后面一半，如果中间点小于尾元素，说明最小数字在前一半。依次循环。
同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            while (rear - front) > 1:
                mid = (rear + front) // 2
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                elif rotateArray[mid] == rotateArray[front] and rotateArray[front] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal

    # 书上方法
    def minNumberInRotateArray2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.MinInOrder(rotateArray, front, rear)

            if rotateArray[midIndex] >= rotateArray[front]:
                front = midIndex
            elif rotateArray[midIndex] <= rotateArray[rear]:
                rear = midIndex
        return rotateArray[midIndex]

    def MinInOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end + 1]:
            if i < result:
                result = i
        return result


if __name__ == '__main__':
    Test = Solution()
    print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
    # print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
    # print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
    # print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
    # print(Test.minNumberInRotateArray([]))
    # print(Test.minNumberInRotateArray([1]))
