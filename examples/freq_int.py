#find the most frequent integer in an array

#input integer array
arr = [1, 1, 2, 2, 2, 2,  1, 3, 4, 5, 5, 5]

#dictionary for storing results
numbers = {}

#in the event there's multiple max values
out = []


for item in arr:
    if not numbers.has_key(item):
        numbers[item] = 1
    else:
        numbers[item] = numbers.get(item) + 1

max_val = numbers[max(numbers, key = numbers.get)]

for item in numbers:
    if numbers[item] == max_val:
        out.append(item)

print out
