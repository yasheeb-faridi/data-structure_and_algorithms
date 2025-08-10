def linear_search(list, target):
    try:
        return list.index(target)
    ## Using Python built-in .index() for speed (implemented in C). Much faster for large lists.
    except ValueError:
        return None

def verify(index):
    if index is not None:
        print(f'Target found at index: {index}')
    else:
        print("Target not found in the list.")

nums = [x for x in range(1, 1000000)]

tar_int = int(input("Enter an integer from 1 to 1000000: "))

result = linear_search(nums, tar_int)
verify(result)
