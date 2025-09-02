import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(tx, proof, pubkey_bytes):
    pubkey = PublicKey.fromString(pubkey_bytes)
    tx_hash = hashlib.sha256(tx.encode()).digest()
    r, s = proof
    sig = pubkey.verify(tx_hash, (r,s))
    return sig


tx = "transfer 10 ETH from 0x123 to 0x456"
proof = (1234567890, 9876543210) #replace with actual proof from zk-SNARK
privkey = PrivateKey()
pubkey_bytes = privkey.publicKey().toString()

verified = verify_zk_proof(tx, proof, pubkey_bytes)

print(verified)

