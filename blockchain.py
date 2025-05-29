import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce, self.hash = self.proof_of_work()

    def calculate_hash(self, nonce):
        text = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    def proof_of_work(self):
        nonce = 0
        prefix = '0' * self.difficulty
        while True:
            hash_value = self.calculate_hash(nonce)
            if hash_value.startswith(prefix):
                return nonce, hash_value
            nonce += 1

class Blockchain:
    def __init__(self):
        self.difficulty = 2
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0", self.difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, last.hash, self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash(curr.nonce):
                print(f"Invalid hash at block {i}")
                return False

            if curr.previous_hash != prev.hash:
                print(f"Invalid previous hash link at block {i}")
                return False

        return True

# Example usage
if __name__ == "__main__":
    my_chain = Blockchain()
    my_chain.add_block("First real block")
    my_chain.add_block("Second block with data")
    my_chain.add_block("Another block after that")

    for block in my_chain.chain:
        print(f"\nBlock {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")

    print("\nBlockchain Valid?", my_chain.is_chain_valid())
