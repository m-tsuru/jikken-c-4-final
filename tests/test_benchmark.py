from sort import (
    generateSortData,
    builtInSort,
    bubbleSort,
    quickSort,
    mergeSort,
    insertionSort,
    selectionSort,
)
import pytest

test_pattern = [1000, 2000, 4000, 8000]
rounds = 100
warmup_rounds = 10


@pytest.mark.parametrize("num", test_pattern)
def test_generateSortData(
    benchmark,
    num: int,
):
    """
    ソート対象のリストを生成するベンチマーク
    """
    data: list[int] = []
    benchmark.pedantic(
        generateSortData,
        args=(data,),
        kwargs={"num": num},
        rounds=rounds,
        warmup_rounds=warmup_rounds,
    )


@pytest.mark.parametrize("num", test_pattern)
def test_builtInSort(
    benchmark,
    num: int,
):
    """
    ソートライブラリを用いたソートリスト
    """
    data: list[int] = []
    generateSortData(data, num)

    def sort():
        return builtInSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)

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

    def sort():
        return bubbleSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)


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

    def sort():
        return quickSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)


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

    def sort():
        return mergeSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)


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

    def sort():
        return selectionSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)


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

    def sort():
        return insertionSort(data.copy())

    benchmark.pedantic(sort, rounds=rounds, warmup_rounds=warmup_rounds)
