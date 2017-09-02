def max_value(the_lists):
    for i in the_lists:
        for j in the_lists:
            if i < j:
                i = j
    return i

a = [23,234,234,234,345,3645,65675,234,234,456,234,12]
b = max_value(a)
print(b)
