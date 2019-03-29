import hashlib
from itertools import chain, product

# simple bruteforce anyone can find on the internet
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

for attempt in bruteforce('abcdefghijklmnopqrstuvwxyz0123456789', 10):
    hash = hashlib.sha256("blockchain-course.org:" + str(attempt)).hexdigest()
    if hash == "02b2ad563f497a01c78fe73e43030520d86421f45db133302750028e1f3ac7e3":
        break

print attempt
