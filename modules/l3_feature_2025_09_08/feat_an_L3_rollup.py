import hashlib
from ellipticcurve.privateKey import PrivateKey

def verify_zk_proof(proof, public_key, commitment, challenge):
    r = proof['r']
    s = proof['s']
    vk =  PrivateKey().publicKey()
    vk.point.x = int(public_key['x'],16)
    vk.point.y = int(public_key['y'],16)
    
    c = int(challenge,16)
    m = hashlib.sha256(commitment.encode()).hexdigest()
    
    lhs = vk.point.scale(c).add(PrivateKey(r).publicKey().point)
    rhs = PrivateKey(s).publicKey().point

    return lhs == rhs
