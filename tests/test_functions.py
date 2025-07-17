from sort import (
    generateSortData,
    builtInSort,
    bubbleSort,
    quickSort,
    mergeSort,
    insertionSort,
    selectionSort,
)

data: list[int] = []
generateSortData(data, 100)
sorted_data = builtInSort(data.copy())


def test_bubbleSort():
    """
    バブルソートを用いたソートリスト
    """
    assert bubbleSort(data.copy()) == sorted_data


def test_quickSort():
    """
    クイックソートを用いたソートリスト
    """
    assert quickSort(data.copy()) == sorted_data


def test_mergeSort():
    """
    マージソートを用いたソートリスト
    """
    assert mergeSort(data.copy()) == sorted_data


def test_insertionSort():
    """
    挿入ソートを用いたソートリスト
    """
    assert insertionSort(data.copy()) == sorted_data


def test_selectionSort():
    """
    選択ソートを用いたソートリスト
    """
    assert selectionSort(data.copy()) == sorted_data
