def solution(array):
    max_val = array[0]
    max_i = 0

    for i, val in enumerate(array):
        if max_val < val:
            max_val = val
            max_i = i

    return [max_val, max_i]