
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarray = dataset[:mid]
        rightarray = dataset[mid:]

        mergeSort(leftarray)
        mergeSort(rightarray)

        i=0
        j=0
        k=0

        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                dataset[k] = leftarray[i]
                i += 1
            else:
                
                dataset[k] = rightarray[j]
                j += 1
            k+=1
        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i += 1
            k += 1

        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j += 1
            k += 1

print(items)
mergeSort(items)
print(items)