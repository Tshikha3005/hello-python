
def solve(nums, k):
    # Create a dictionary to store the value and its index
    # seen = { value: index }
    seen = {}

    for i, num in enumerate(nums):
        # Calculate what number we need to reach the target k
        complement = k - num

        # If that number is already in our dictionary, we found the pair!
        if complement in seen:
            return [seen[complement], i]

        # Otherwise, save the current number and its index and move on
        seen[num] = i

    return [] # Return empty if no pair is found
print(solve([2,7,11,15], 9))