import time

tar_int = int(input("Enter an integer from 1 to 1000000: "))

start_time = time.perf_counter()

nums = list(range(1, 1000000))
result = nums.index(tar_int) if tar_int in nums else None
print(f"The target {tar_int} found at index: {result}")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds.")