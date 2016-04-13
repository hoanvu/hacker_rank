import re

def filter_email(email):
    pattern = r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z0-9]{3}$'
    match = re.search(pattern, email)
    if match:
        return True
    else:
        return False
    
t = int(raw_input())
emails = []
for a0 in xrange(t):
    emails.append(raw_input())
    
emails = list(filter(lambda email: filter_email(email), emails))
emails.sort()
print emails
