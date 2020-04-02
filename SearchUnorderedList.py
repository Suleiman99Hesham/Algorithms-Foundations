items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def searchInUOList(item,itemList):
    for i  in range(0,len(items)):
        if item == itemList[i]:
            return i;
    return None

print(searchInUOList(87,items))
print(searchInUOList(250,items))