from sort import generateSortData, sortLibSort, bubbleSort
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
