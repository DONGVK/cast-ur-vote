"""
*   app.py
*   @Author : DONG
"""
__author__ = "DONG"

import datetime
import hashlib
import json


class Blockchain:
    # Initialize the first block
    def __init__(self):
        self.chain = []
        self.pending = []

        self.create_block(proof=1, previous_hash='0')
        
    # Add a block into the chain
    def create_block(self, proof, previous_hash = None):
        block = {'index': len(self.chain) + 1,
				'timestamp': str(datetime.datetime.now()),
                'data' : self.pending,
				'proof': proof,
				'previous_hash': previous_hash or self.hash(self.previous_block())
        }
        self.chain.append(block)
        return block
		
    # Search the blockchain for the most recent block.
    def previous_block(self):
        return self.chain[-1]
		
	# This is the function for proof of work and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '00000':
                check_proof = True
            else:
                new_proof += 1
				
        return new_proof

    # Enrypt the block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # Add a chain
    def new_transaction(self, sender, candidate):
        transaction = {
            'sender': sender,
            'candidate': candidate,
        }
        self.pending.append(transaction)
        return self.previous_block()['index'] + 1

    # Check if the chain is valid
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
		
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
				
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != '00000':
                return False
            previous_block = block
            block_index += 1
            
        return True

blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike")
t2 = blockchain.new_transaction("Mike", "Satoshi")
t3 = blockchain.new_transaction("Satoshi", "Hal Finney")
blockchain.create_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice")
t5 = blockchain.new_transaction("Alice", "Bob")
t6 = blockchain.new_transaction("Bob", "Mike")
blockchain.create_block(6789)

print(blockchain.chain)
