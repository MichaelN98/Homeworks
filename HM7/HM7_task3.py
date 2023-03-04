from typing import Callable, List, Tuple, Union
def my_map(function: Callable, sequence: Union[List[int], List[float], List[str]]) -> List[Union[int, float, str]]:
    result = []
    for item in sequence:
        result.append(function(item))
    return result
