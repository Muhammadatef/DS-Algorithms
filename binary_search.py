def binary_search(list, item):
    # Initialize the low and high pointers to the beginning and end of the list, respectively.
    low = 0
    high = len(list) - 1

    # Continue the loop until low pointer is not greater than high pointer.
    while low <= high:
        # Calculate the middle index by taking the average of low and high and flooring the result.
        mid = (low + high) // 2
        # Retrieve the element at the middle index.
        guess = list[mid]

        # If the element at mid is the item we're searching for, return the mid index.
        if guess == item:
            return mid
        # If the guessed element is greater than the item, move the high pointer below the mid index.
        if guess > item:
            high = mid - 1
        # If the guessed element is less than the item, move the low pointer above the mid index.
        else:
            low = mid + 1
    
    # If the loop ends without returning, the item is not in the list.
    return None

# Example list and item to search
my_list = [1, 2, 3, 4, 6, 8, 10]
# Print the result of the binary search
print(f"The index for the binary search algorithm is {binary_search(my_list, 10)}")


# Big O Notation Explanation:
# Binary search has a time complexity of O(log n) where n is the number of elements in the list.
# This is because the algorithm divides the search space in half with each iteration,
# logarithmically reducing the size of the search space.
# The space complexity is O(1) as it uses a constant amount of space regardless of the input size.




##Explanation of Big O Notation:

##Time Complexity (O(log n)): The loop in the binary search halves the number of elements considered with each iteration, 
##so the time to complete the search grows logarithmically in relation to the size of the list. This makes binary search particularly 
##efficient for searching in large data sets.

##Space Complexity (O(1)): The binary search algorithm uses a constant amount of space (only variables for low, high, mid, and guess) during its execution, 
##so its space complexity does not depend on the size of the input list.

##This concise treatment of Big O notation provides an understanding of why binary search is more efficient than simpler search methods, like linear search, especially as the size of the data increases.