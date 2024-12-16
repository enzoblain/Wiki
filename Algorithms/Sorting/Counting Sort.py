import numpy as np

def countingSort(arr: np.ndarray) -> int:
    """
    Algorithm: Counting Sort
    Explanation:
        - A non-comparison-based sorting algorithm, effective for sorting integers within a limited range.
        - Works by counting the occurrences of each element in the input array and using this information to place the elements in sorted order.
        - Steps:
            1. Count the occurrences of each element and store them in a counting array.
            2. Compute cumulative counts to determine the positions of elements in the sorted array.
            3. Populate the output array by placing each element at its correct position using the cumulative counts.
        - Suitable for arrays with non-negative integers and a small range of values.
    
    Time Complexity: O(n + k), where `n` is the number of elements in the array and `k` is the range of input values.
    Space Complexity: O(n + k) for the counting array and the output array.
    """
    max_val = max(arr)

    counting_arr = np.zeros(max_val + 1, dtype=int)
    output_arr = np.zeros(len(arr), dtype=int)

    for val in arr:
        counting_arr[val] += 1
    
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]
    
    for val in arr:
        output_arr[counting_arr[val] - 1] = val
        counting_arr[val] -= 1

    return output_arr

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.random.choice(range(100), size=size, replace=False)
    print(f"Array: {arr}")
    print(f"Sorted Array: {countingSort(arr)}")