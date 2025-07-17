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
