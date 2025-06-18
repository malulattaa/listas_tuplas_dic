def count_sublists(*args):
    count = 0
    for item in args:
        if isinstance(item, list):
            count += 1 + count_sublists(*item)
    return count

print(count_sublists(2,3,5,6,[1,3,4], [2, 3, [1, 2, 3,[1,2]]]))
