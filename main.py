# block chain example 3
# refrence : https://geekflare.com/create-a-blockchain-with-python/

import hashlib


class GeekCoinBlock:
    
    # initialing constructor
    def __init__(self, previous_block_hash, transaction_list):
        
        self.previous_block_hash = previous_block_hash # reference to previous block
        self.transaction_list = transaction_list # transaction made in current block

        # we do not save block data in string for real projects
        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"

        # hashing block data and generating hash for that block
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # refer hashlib.txt



# t1 = "Noah sends 5 GC to Mark"
# t2 = "Mark sends 2.3 GC to James"
# t3 = "James sends 4.2 GC to Alisson"
# t4 = "Alisson sends 1.1 GC to Noah"


# block1 = GeekCoinBlock('firstblock', [t1,t2])

# print(f"Block 1 data: {block1.block_data}")
# print(f"Block 1 hash: {block1.block_hash}")


# block2 = GeekCoinBlock(block1.block_hash, [t3,t4])

# print(f"Block 2 data: {block2.block_data}")
# print(f"Block 2 hash: {block2.block_hash}")




class BlockChain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(GeekCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i+1}: {self.chain[i].block_data}")
            print(f"Hash {i+1}: {self.chain[i].block_hash}\n")


    @property
    def last_block(self):
        return self.chain[-1]


# Testing
t1 = "George sends 3.1 GC to Joe"
t2 = "Joe sends 2.5 GC to Adam"
t3 = "Adam sends 1.2 GC to Bob"
t4 = "Bob sends 0.5 GC to Charlie"
t5 = "Charlie sends 0.2 GC to David"
t6 = "David sends 0.1 GC to Eric"

myblockchain = BlockChain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()