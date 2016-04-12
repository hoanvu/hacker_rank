# Hacker Rank - Sort Data
# https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort

# Extract shapes of data from the first line
row, col = map(int, raw_input().strip().split(' '))

# Extract data
data = []
for r in xrange(row):
    data.append(raw_input().strip().split(' '))

# Extract k
k = int(raw_input().strip())

output = []
for row in data:
    # If output list is empty, append the first list into output
    if len(output) == 0:
        output.append(row)
    # Otherwise, append and sort the output list
    else:
        output.append(row)
        output.sort(key=lambda row: int(row[k]))

# Print the result
for r in output:
    print ' '.join(r)
