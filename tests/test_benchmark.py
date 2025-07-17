from sort import (
    generateSortData,
    sortLibSort,
    bubbleSort,
    quickSort,
    mergeSort,
    insertionSort,
    selectionSort,
)
import pytest

test_pattern = [1000, 2000, 4000, 8000]


@pytest.mark.parametrize("num", test_pattern)
def test_generateSortData(
    benchmark,
    num: int,
):
    """
    ソート対象のリストを生成するベンチマーク
    """
    data: list[int] = []
    benchmark(generateSortData, data, num)


@pytest.mark.parametrize("num", test_pattern)
def test_sortdata(
    benchmark,
    num: int,
):
    """
    ソートライブラリを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(sortLibSort, data)


@pytest.mark.parametrize("num", test_pattern)
def test_bubbleSort(
    benchmark,
    num: int,
):
    """
    バブルソートを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(bubbleSort, data)


@pytest.mark.parametrize("num", test_pattern)
def test_quickSort(
    benchmark,
    num: int,
):
    """
    クイックソートを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(quickSort, data)


@pytest.mark.parametrize("num", test_pattern)
def test_mergeSort(
    benchmark,
    num: int,
):
    """
    マージソートを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(mergeSort, data)


@pytest.mark.parametrize("num", test_pattern)
def test_selectionSort(
    benchmark,
    num: int,
):
    """
    選択ソートを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(selectionSort, data)


@pytest.mark.parametrize("num", test_pattern)
def test_insertionSort(
    benchmark,
    num: int,
):
    """
    挿入ソートを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)
    benchmark(insertionSort, data)
