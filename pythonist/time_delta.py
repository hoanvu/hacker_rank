# Hacker Rank - Time Delta
# https://www.hackerrank.com/contests/pythonist/challenges/python-time-delta

import datetime

inputs = int(input())
for _ in range(inputs):
    t1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    delta = t1 - t2
    print(abs(int(delta.total_seconds())))
