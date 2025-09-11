"""
Binary Search only works with ordered lists (arrays)
Has a complexity of O(n*log(n))
"""
def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1
    while first <= last:
        middle = (last + first) // 2
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False

list_ = [2, 4, 6, 8, 10, 12, 14]
print(binary_search(list_, 4))
print(binary_search(list_, 12))
print(binary_search(list_, 10))
print(binary_search(list_, 1))
