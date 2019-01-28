def my_strrev(ary):
    str = list(ary)
    print(str)
    for i in range(len(str)//2):
        t = ary[i]
        str[i] = str[len(str)-1-i]
        str[len(ary)-1-i] = t
    ary = "".join(str)
    return ary

ary = "abcdef"
ary = my_strrev(ary)
print(ary)