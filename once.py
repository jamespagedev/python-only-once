# Given an array where every element occurs three
# times, except one element which occurs only once.
# Find the element that occurs once.
#
# Example: [1, 3, 2, 5, 4, 3, 2, 5, 1, 2, 3, 1, 5] => 4
# Example sorted: [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5] => 4

import time
import operator
import random

# Runtime complexity: 0(n)
# Space complexity:   0(n)


def first_pass_once(arr):
    # Create dictionary
    count = {}
    # Store count of all elements in dictionary
    for element in arr:
        if element not in count:
            count[element] = 0
        count[element] += 1
    # Print element with smallest count
    single_element = min(count.items(), key=operator.itemgetter(1))[0]
    print(single_element)

# Runtime complexity: 0(n log n)
# Space complexity:   0(1)


def second_pass_once(arr):
    # Sort all elements
    arr.sort()  # python sort is Timsort - O(n log n)

    # Edge case - first element
    if arr[0] != arr[1]:
        print(arr[0])
        return
    # Edge case - last element
    if arr[len(arr) - 1] != arr[len(arr) - 2]:
        print(arr[len(arr) - 1])
        return
    # General case - middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            print(arr[i])
            return


# Generate big array of triples
arr1 = []
for i in range(200000):
    # Skip this value, it will be our singleton
    if i != 111111:
        arr1.insert(random.randint(0, len(arr1)), i)
        arr1.insert(random.randint(0, len(arr1)), i)
        arr1.insert(random.randint(0, len(arr1)), i)
# Insert the singleton into a random location
arr1.insert(random.randint(0, len(arr1)), 111111)

# Try it out!
start_time = time.time()
first_pass_once(arr1)
end_time = time.time()
print(f"1st pass runtime: {end_time - start_time} seconds\n")

start_time = time.time()
second_pass_once(arr1)
end_time = time.time()
print(f"2nt pass runtime: {end_time - start_time} seconds\n")
