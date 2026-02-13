# pass multiple *args

def sum_all(*args):
    return sum(args)


print(sum_all(1,4))
print(sum_all(1,4,8,9))
print(sum_all(1,4,8,9,8,3,5,2))