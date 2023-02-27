from typing import Callable, Sequence, TypeVar

T = TypeVar('T')

def filter_seq(callback: Callable[[T], bool], sequence: Sequence[T]) -> Sequence[T]:
    return [elem for elem in sequence if callback(elem)]
