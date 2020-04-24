items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def findmax(itemlist):
    if len(itemlist) == 1:
        return itemlist[0]
    op1 = itemlist[0]
    op2 = findmax(itemlist[1:])
    print(op1, "---", op2)
    if op1 >= op2:
        return op1
    else:
        return op2


print(findmax(items))
