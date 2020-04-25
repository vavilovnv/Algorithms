#Быстрая сортировка
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i<=pivot]
        greater = [i for i in arr[1:] if i>pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([11, 5, 2, 7, 15]))
