# Пожалуйста, решите следующую простую задачу. Можно использовать любые инструменты.
# Дано: список dict-объектов вида вида {"key": "value"}, например:
# [
# {"key1": "value1"},
# {"k1": "v1", "k2": "v2", "k3": "v3"},
# {},
# {},
# {"key1": "value1"},
# {"key1": "value1"},
# {"key2": "value2"}
# ]
# Напишите функцию, которая удаляет дубликаты из этого списка.
# Для примера выше возвращаемое значение может быть равно
# [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
# Обязательное условие: функция не должна иметь сложность O(n^2).

from typing import List


def remove_duplicate(array: List[dict]) -> List:
    unique_array = []
    for elem in array:
        if elem not in unique_array:
            unique_array.append(elem)
    print(unique_array)


array = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"}
]

remove_duplicate(array)
