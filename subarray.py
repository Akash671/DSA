def get_all_subarrays(arr):
    """
    Calculates all subarrays of an array using nested loops.

    Args:
        arr: The input array.

    Returns:
        A list of lists, where each inner list is a subarray.
    """
    n = len(arr)
    subarrays = []
    for i in range(n):  # Iterate through starting indices
        for j in range(i, n):  # Iterate through ending indices
            subarrays.append(arr[i:j+1])
    return subarrays

# Example usage:
my_array = [1, 2, 1]
all_subarrays = get_all_subarrays(my_array)
print(all_subarrays)  # Output: [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]