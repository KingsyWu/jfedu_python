
def power(x, n):
    s = 1
    for i in n:
        n = n - 1
        s = s * x
    return s
p = power(5, 4)
print(p)