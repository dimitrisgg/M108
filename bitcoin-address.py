import hashlib
import base58
from ecdsa import SigningKey, SECP256k1


# PARAMETERS
network_prefix = '6f'     # testnet (if mainnet then '00')
h_ripemd160 = hashlib.new('ripemd160')
compressed_prefix_even = '02'
compressed_prefix_odd = '03'
private_key_raw = "2bc7c746a3b554f2926bfd506a8345143faa884945ef75b3b332e6bdefc7eb41"

# SigningKey object
private_key = SigningKey.from_string(private_key_raw.decode('hex'), curve=SECP256k1)

# Get public key. Returns both X,Y concatenated
public_key_raw = private_key.get_verifying_key().to_string().encode('hex')

# Compress public key
if (int(public_key_raw[-1], 16) % 2) == 0:
    compressed_prefix = compressed_prefix_even
else:
    compressed_prefix = compressed_prefix_odd
# keep only the first point on the elliptic curve with a prefix
compressed_public_key_raw = (compressed_prefix + public_key_raw)[:66]

# Payload
h_ripemd160.update(hashlib.sha256(compressed_public_key_raw.decode('hex')).digest())
encrypted_pk_raw = h_ripemd160.hexdigest()

# Prepend network on the payload
net_encrypted_pk_raw = network_prefix + encrypted_pk_raw

# Compute checksum and pick first 4 bytes
checksum = hashlib.sha256(hashlib.sha256(net_encrypted_pk_raw.decode('hex')).digest()).hexdigest()[:8]

# Append checksum on payload
net_encrypted_pk_checksum_raw = net_encrypted_pk_raw + checksum

# encode on base58
address = base58.b58encode(net_encrypted_pk_checksum_raw.decode('hex'))
print "Bitcoin address:" + address

