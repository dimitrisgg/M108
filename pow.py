import hashlib
import random
import sys

nonce = random.randint(1,sys.maxsize)/2

while True:
    hash = hashlib.sha256("blockchain-course.org:65" + str(nonce)).hexdigest()
    if hash.startswith("00000"):
        break
    nonce += 1

print nonce
