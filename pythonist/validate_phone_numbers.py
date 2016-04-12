# Hacker Rank - Validating phone numbers
# https://www.hackerrank.com/contests/pythonist/challenges/validating-the-phone-number

import re

t = int(input())
for i in range(t):
    phone = str(raw_input().strip())
    if phone.isdigit():
        match = re.search(r'^[789][\d]{9}$', phone)
        print "YES" if match else "NO"
    else:
        print "NO"
