items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist, low, high):
    mid = (low + high) // 2
    if low > high:
        return None
    if item == itemlist[mid]:
        return mid
    elif item > itemlist[mid]:
        return binarysearch(item, itemlist, mid + 1, high)
    else:
        return binarysearch(item, itemlist, low, mid - 1)


result = binarysearch(53, items, 0, len(items) - 1)
print(result)
print(binarysearch(250,items,0,len(items)-1))
