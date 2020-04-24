def quickSort (dataValues,start,end):
    if start < end:
        pvtIndx = partition(dataValues, start, end)

        quickSort(dataValues, start, pvtIndx-1)
        quickSort(dataValues, pvtIndx+1, end)

def partition (dataValues, start, end):
    pvtElement=dataValues[start]
    lower=start+1
    upper=end

    done=False
    while not done:
        while lower <= upper and dataValues[lower] <= pvtElement:
            lower += 1
        while lower <= upper and dataValues[upper] >= pvtElement:
            upper -= 1
        if upper < lower:
            done=True
        else:
            temp = dataValues[lower]
            dataValues[lower] = dataValues[upper]
            dataValues[upper] = temp
    temp = dataValues[start]
    dataValues[start] = dataValues[upper]
    dataValues[upper] = temp

    return upper


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
print(items)
quickSort(items, 0, len(items)-1)
print(items)
