'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_values = []

    for i in range(k - 1, len(nums)):
        largest_number = max(nums[i-k+1 : i+1])
        max_values.append(largest_number)
    
    return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3

    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

    k = 2  

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")