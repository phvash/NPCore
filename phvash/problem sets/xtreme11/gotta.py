def max_subarray_sum(array, n):
    if len(array) == 1:
        return array[0]
    
    mid_point = n//2
    left_subarray = array[:mid_point]
    right_subarray = array[mid_point:]
    # print("left sub array: ", left_subarray)
    # print("right sub array: ", right_subarray)
    left_mss = max_subarray_sum(left_subarray, len(left_subarray))
    right_mss = max_subarray_sum(right_subarray, len(right_subarray))
    max_crossing_subarray = find_max_crossing_sum(array, 0, mid_point, n)
    # print(left_mss, right_mss, max_crossing_subarray)
    return max(left_mss, right_mss, max_crossing_subarray)

def find_max_crossing_sum(array, start_index, mid_point, end_index):
    left_sum = float('-inf')
    sum = 0
    for index in range(mid_point-1, -1, -1):
        sum += array[index]
        if sum > left_sum:
            left_sum = sum
        # print("sum: {}, left_sum:{}".format(sum, left_sum))

    right_sum = float('-inf')
    sum = 0
    for index in range(mid_point, end_index):
        sum += array[index]
        if sum > right_sum:
            right_sum = sum
        # print("sum: {}, right_sum:{}".format(sum, right_sum))

    return left_sum + right_sum
    

if __name__ == '__main__':
    array = []
    r, c = input().strip(" ").split(" ")
    y = int(r) + int(c) - 2
    for i in range(int(r)):
        array += [int(v) for v in input().strip(" ").split(" ")]
    print(max_subarray_sum([0, -2, 0, 2], 2))
    # print(max_subarray_sum([0, 1, 2, -2, -9, -4, -8, 5, 0], 4))
    # print(max_subarray_sum(array, y))


