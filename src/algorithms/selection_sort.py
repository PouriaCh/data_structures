from typing import List


def selection_sort(input_list: List[int]) -> List[int]:
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j
        input_list[min_index], input_list[i] = input_list[i], input_list[min_index]
    return input_list


print(selection_sort([4, 2, 6, 5, 1, 3]))
