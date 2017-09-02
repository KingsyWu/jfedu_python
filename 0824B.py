def min_value(the_lists):
    # 取最小值
    for i in the_lists:
        for j in the_lists:
            if i > j:
                i = j
    return i


def auto_sort(the_lists):
    # 吉林-王殿懿的思路
    new_lists = []
    for i in range(0, len(the_lists)):
        min_val = min_value(the_lists)
        the_lists.remove(min_val)
        new_lists = new_lists.extend(min_val)
    return new_lists

a = [23, 234, 234, 234, 345, 3645, 5675, 234, 234, 456, 234, 12]
b = auto_sort(a)
print(b)
