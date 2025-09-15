from eth_utils import to_checksum_address

class FeeManager:
    def __init__(self, owner, l3_chain_id):
        self.owner = to_checksum_address(owner)
        self.l3_chain_id = l3_chain_id
        self.fee_amount = 0
        self.fee_recipient = "0x0000000000000000000000000000000000000000"

    def setFee(self, amount, recipient):
        assert msg.sender == self.owner, "Only owner can set fee."
        self.fee_amount = amount
        self.fee_recipient = to_checksum_address(recipient)

    def getFee(self):
        return self.fee_amount

    def getRecipient(self):
        return self.fee_recipient

    def payFee(self, application_id):
        assert msg.value >= self.fee_amount, "Insufficient fee."
        send(self.fee_recipient, self.fee_amount)
        # Application-specific logic using application_id goes here...
        return True

    def getChainId(self):
        return self.l3_chain_id
