# coding:utf-8
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]      #将第一个值做为基准
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)      #得到第一轮分组之后，继续将分组进行下去。
        more = quickSort(more)

        return less + pivotList + more

if __name__ == '__main__':
    nums = [9, 3, 5, 8, 2, 7, 1]
    print quickSort(nums)
