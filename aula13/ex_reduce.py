from functools import reduce

def count_sublists_reduce(*args):
    return reduce(lambda count, item:count + (1 if isinstance(item, list) else 0), args, 0)

print(count_sublists_reduce(2,3,5,6,[1,3,4], [2, 3]))