# сортировка выбором
def findSmallest(arr):
    smallest = arr[0] #хранение наименьшего значения
    smallest_index = 0 #хранение индекса наименьшего значения
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smalest = findSmallest(arr)
        newArr.append(arr.pop(smalest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))