#find the most frequent integer in an array

#uses commandline arguments for input file and json to process
import sys, json

#reads first argument as input file in json list format
#basic error handling
try:
    with open(sys.argv[1]) as f:
        arr = json.load(f)
except IOError:
    print "File Not Found!"
    exit()
except IndexError:
    print "Input File Argument!"
    exit()
except ValueError:
    print "Check Input File Formatting!"
    exit()

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
