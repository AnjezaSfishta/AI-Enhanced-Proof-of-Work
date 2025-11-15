import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            (str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)).encode('utf-8')
        ).hexdigest()

    def mine_block(self):
        target = '0' * self.difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", 4)

def create_new_block(previous_block):
    return Block(previous_block.index + 1, previous_block.hash, time.time(), "Block Data", 4)
