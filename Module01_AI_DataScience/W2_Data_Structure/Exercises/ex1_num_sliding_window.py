def max_kernel(num_list, sliding_size):
    result = [] # Empty list

    # Loop with index from 0 to the third last element
    for index in range(len(num_list) - sliding_size + 1):
        # Find the max within the sliding window
        max_value = max(num_list[index : index + sliding_size])

        # Add to the result list
        result.append(max_value)

    return result


# TESTING OF THE FUNCTION
sliding_size = 3
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] 
result = max_kernel(num_list, sliding_size)
print(result)

sliding_size = 3
num_list = [3, 4, 5] 
sliding_size = 3
result = max_kernel(num_list, sliding_size)
print(result)


# NOTE:
# - Slicing allows you to get a subset of the list.
# - The syntax is `list[start:stop:step]`.
# - `start` is the starting index, `stop` is the stopping index (exclusive), and `step` is the step value.

# range(n) : start from 0 to n - 1



# TRAC NGHIEM 1
assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))  # Output: [5, 5, 5, 5, 10, 12, 33, 33] 
#Answer: a)