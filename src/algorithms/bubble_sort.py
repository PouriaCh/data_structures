from typing import List


def bubble_sort(input_list: List[int]) -> List[int]:
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list


print(bubble_sort([4, 1, 5, 6, 3, 2]))
