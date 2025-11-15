import sys

if len(sys.argv) >= 2:
    script_name = sys.argv[0]
    array = [None] * 11
    array[1] = sys.argv[1]
else:
    array = [1,2,3,9,7,10,5]

sum_of_elements = sum(array)
print("Sum of elements:", sum_of_elements)
avg_of_elements = sum_of_elements / len(array)
print("Average of elements:", avg_of_elements)

print("Max elements:", max(array))
print("Min elements:", min(array))
