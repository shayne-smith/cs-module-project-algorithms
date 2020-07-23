'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# O(n^2)
def single_number_slow(arr):
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

#O(n)
def single_number(arr):
    # space complexity: O((1/2) * n)
    # time complexity: O(1)
    s = set()

    # space complexity: O(n)
    for x in arr: #O(n)
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    
    return list(s)[0] 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")