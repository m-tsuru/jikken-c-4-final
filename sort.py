import random


def generateSortData(data: list, num: int = 8000):
    """
    ソート対象のリストを生成
    data: リスト
    num: 追加する個数
    """
    for i in range(num):
        data.append(random.randint(0, num))


def sortLibSort(data) -> list[int]:
    """
    リスト型のソートメソッドを利用して、データをソート
    """
    data.sort()
    return data

def bubbleSort(data):
    num = len(data)
    for i in range(num - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    return data

def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def selectionSort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left_half = mergeSort(data[:mid])
    right_half = mergeSort(data[mid:])
    return merge(left_half, right_half)


def quickSort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quickSort(left) + middle + quickSort(right)
