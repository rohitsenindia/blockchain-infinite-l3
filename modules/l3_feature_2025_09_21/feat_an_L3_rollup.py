import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(tx, proof, vk):
    h = hashlib.sha256()
    h.update(tx.encode())
    tx_hash = h.digest()

    try:
        pk = PublicKey.from_point(vk['x'], vk['y'], curve='secp256k1')
        sig = proof['signature']
        r = proof['r']
        s = proof['s']

        return pk.verify(tx_hash, sig) and pk.verify_schnorr(tx_hash, r, s)

    except (ValueError, KeyError, TypeError):
        return False

tx = "TransactionData"
proof = {'signature': b'some_signature', 'r': b'some_r', 's': b'some_s'}
vk = {'x': b'some_x', 'y': b'some_y'}

is_valid = verify_zk_proof(tx, proof, vk)
print(is_valid)
