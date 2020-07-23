'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    # determine number of non-zero values
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            count += 1

    # loop through input array
    i = 0
    while i < len(arr):

        # if a zero is encountered and index is in non-zero part of array
        # pop current zero and append to end
        while arr[i] == 0 and i < count:
            arr.pop(i)
            arr.append(0)

        i += 1
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")