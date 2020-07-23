'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    newArr = []

    # loop through input array
    for index, elem in enumerate(arr):
        # if element hasn't been seen before add to newArr array and remove from input array
        if elem not in newArr:
            newArr.append(elem)
            arr.pop(index)

    # loop through both arrays and find odd element out
    for elem in newArr:
        if elem not in arr:
            return elem

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")