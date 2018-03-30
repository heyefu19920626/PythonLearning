import random






def swap(arry, index_a, index_b):
    [arry[index_a], arry[index_b]] = [arry[index_b], arry[index_a]]



def bubble_sort(arry):
    """ 冒泡排序 """
    length = len(arry)
    start = 0
    i = start
    end = length - 1
    while end > start:
        # 从左往右
        while i < end:
            if arry[i] > arry[i+1]:
                swap(arry, i, i+1)
            i += 1
        # 从右往左
        while i > start:
            if arry[i] < arry[i-1]:
                swap(arry, i, i-1)
            i -= 1
        end -= 1
        start += 1
        i = start


arry = [random.randint(1, 100) for i in range(100)]
print(arry)
bubble_sort(arry)
print(arry)
