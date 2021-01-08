numbers = [5, 7, 10, 2]

def decrement_list(num_list):
    return list(map(lambda x: x - 1, num_list))


print(decrement_list(numbers))

