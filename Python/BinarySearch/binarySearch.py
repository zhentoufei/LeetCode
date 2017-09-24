# coding:utf8
def binary_search(lst, value, low, high):  # low,high是lst的查找范围
    if high < low:
        return -1
    mid = (low + high) / 2  # 在此处自动向下取整
    if lst[mid] > value:
        return binary_search(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binary_search(lst, value, mid + 1, high)
    else:
        return mid


def b_search(l, value):
    lo, hi = 0, len(l) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

def bs(arr, val):
    lo = 0
    hi = len(arr)-1
    # [lo,..., hi]
    while lo<=hi:
        mid = (lo+hi)/2

        if arr[mid]>val:
            hi = mid-1
        elif arr[mid]<val:
            lo = mid+1
        else:
            return



if __name__ == '__main__':
    l = range(50)
    print binary_search(l, 10, 0, 49)
    print b_search(l, 10)
