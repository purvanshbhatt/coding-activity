def sort(numbers):
    # Bubble sort implementation
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def sort_and_find_median(numbers):
    sort(numbers)
    n = len(numbers)
    
    if n == 0:
        return 0
    
    # Calculate median based on length
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]

# Main program
print("Median Calculator")

# Test with a list
test_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Test list: {test_list}")
print(f"Median: {sort_and_find_median(test_list)}")

# User input
user_input = input("\nEnter numbers separated by space: ")
if user_input:
    nums = [float(x) for x in user_input.split()]
    print(f"Median: {sort_and_find_median(nums)}")
