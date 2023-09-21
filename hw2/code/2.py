from typing import List, Tuple


class AdvansedList:
    """
    Вам дан массив из n элементов и список из m запросов
    add(x, l, r): прибавить x к каждому элементу на отрезке [l, r].
    За O(n + m) выведите массив,
    получающийся из исходного после выполнения заданных запросов
    """

    def __init__(self, data: List[int]) -> None:
        self.data: List[int] = data
        self.modifications: List[int] = [0 for i in data]

    def add(self, x: int, l: int, r: int):
        self.modifications[l] += x
        if r < len(self.data):
            self.modifications[r] -= x

    def sync(self):
        acc = 0
        for i, x in enumerate(self.modifications):
            acc += x
            self.data[i] += acc
        self.modifications = [0 for i in self.data]

    def apply_adds(self, qeries: List[Tuple[int, int, int]]):
        for args in qeries:
            self.add(*args)
        self.sync()
        return self.data


def tests():
    assert AdvansedList([0, 0, 0, 0, 0]).apply_adds([]) == [0, 0, 0, 0, 0]
    assert AdvansedList([0, 0, 0, 0, 0]).apply_adds([(1, 0, 4)]) == [
        1,
        1,
        1,
        1,
        0,
    ]
    assert AdvansedList([0, 0, 0, 0, 0]).apply_adds([(1, 0, 5)]) == [
        1,
        1,
        1,
        1,
        1,
    ]
    assert AdvansedList([0, 0, 0, 0, 0]).apply_adds([(1, 0, 5), (2, 4, 5)]) == [
        1,
        1,
        1,
        1,
        3,
    ]


tests()
