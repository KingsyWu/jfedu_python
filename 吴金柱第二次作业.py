def insert_sort(the_lists):
    # 插入排序
    count = len(the_lists)
    for i in range(1, count):
        key = the_lists[i]
        j = i - 1
        while j >= 0:
            if the_lists[j] > key:
                the_lists[j + 1] = the_lists[j]
                the_lists[j] = key
                # print(the_lists)
            j = j - 1
    return the_lists


def shell_sort(the_lists):
    # 希尔排序
    count = len(the_lists)
    step = 3
    group = count // step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = the_lists[j]
                while k >= 0:
                    if the_lists[k] > key:
                        the_lists[k + group] = the_lists[k]
                        the_lists[k] = key
                    k = k - group
                    # print(the_lists)
                j = j + group
        group = group // step
    return the_lists


def bubble_sort(the_lists):
    # 冒泡排序
    count = len(the_lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if the_lists[i] > the_lists[j]:
                the_lists[i], the_lists[j] = the_lists[j], the_lists[i]
                # print(the_lists)
    return the_lists


def quick_sort(the_lists, low, high):
    # 快速排序
    if low > high:
        return the_lists
    key = the_lists[low]
    i = low
    j = high
    print("第" + str(i) + "次递归")
    while i < j:
        while i < j and the_lists[j] >= key:
            j = j - 1
        the_lists[i] = the_lists[j]
        # print(the_lists)
        while i < j and the_lists[i] <= key:
            i = i + 1
        the_lists[j] = the_lists[i]
        print(key)
        print(the_lists)
    the_lists[i] = key
    quick_sort(the_lists, i, low - 1)
    quick_sort(the_lists, low + 1, high)
    return the_lists


    return the_lists




def heap_sort(the_lists):
    # 堆排序
    return the_lists


def merge_sort(the_lists):
    # 归并排序
    return the_lists


def radix_sort(the_lists):    # 基数排序
    return the_lists


def max_value(the_lists):
    # 取最大值
    for i in the_lists:
        for j in the_lists:
            if i < j:
                i = j
    return i


def auto_sort(the_lists):
    # 吉林-王殿懿的思路
    new_lists = []
    for i in range(0, len(the_lists)):
        max_val = max_value(the_lists)
        the_lists.remove(max_val)
        new_lists.insert(0, max_val)
    return new_lists


if __name__ == "__main__":
    a = [1, 15, 3, 6, 2, 14, 4, 28, 18, 10, 8]
    # b = insert_sort(a)
    # b = shell_sort(a)
    # b = bubble_sort(a)
    # b = quick_sort(a, 0, 10)
    b = auto_sort(a)
    print(b)