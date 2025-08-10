## To Avoid Double Scanning 
## The two scans are when the element exists (one for `in` and one for `index`) 
## So the search cost is roughly 2x a linear scan
## Using try-catch block I am doing only one scan when the element exists
## There is also a little cost for Raising an Exception

import time

tar_int = int(input("Enter an integer from 1 to 1000000: "))

start_time = time.perf_counter()

nums = list(range(1, 1000000))

try:
    result = nums.index(tar_int) 
except ValueError:
    result = None
    
print(f"The target {tar_int} found at index: {result}")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds.")