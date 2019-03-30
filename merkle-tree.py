import hashlib

A = "cute"
B = "fox"
C = "oppose"
D = "motor"

hA = hashlib.sha256(A).hexdigest()
hB = hashlib.sha256(B).hexdigest()
hC = hashlib.sha256(C).hexdigest()
hD = hashlib.sha256(D).hexdigest()

h_hAhB = hashlib.sha256(hA + hB).hexdigest()
h_hChD = hashlib.sha256(hC + hD).hexdigest()

MTR = hashlib.sha256(h_hAhB + h_hChD).hexdigest()

print MTR
