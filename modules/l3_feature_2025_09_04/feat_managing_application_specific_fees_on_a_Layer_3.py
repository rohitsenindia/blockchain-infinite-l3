from eth_utils import to_wei

class FeeManager:
    def __init__(self, initial_fee=to_wei(0.1, 'ether')):
        self.fee = initial_fee
        self.owner = msg.sender

    def setFee(self, new_fee):
        assert msg.sender == self.owner, "Only the owner can change the fee."
        self.fee = new_fee

    def getFee(self):
        return self.fee

    def payFee(self):
        assert msg.value >= self.fee, "Insufficient funds to pay fee."
        self.owner.transfer(msg.value)
        self.emitFeePaid(msg.sender, msg.value)

    event FeePaid(address indexed payer, uint256 amount);

    def emitFeePaid(self, payer, amount):
        log.FeePaid(payer, amount)
