import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, data):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'data': data,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Adding a new transaction
    blockchain.add_transaction(sender="DoctorA", recipient="PatientB", data="HealthRecord123")

    # Mining a new block
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(blockchain.last_block)
    blockchain.create_block(proof, previous_hash)

    # Display the blockchain
    print(json.dumps(blockchain.chain, indent=4))



# import json
# import requests
# from web3 import Web3
# from ml_model import train_ml_model
# from data_visualization import visualize_data

# # Load ABI and contract address
# def load_contract_info(path='ml/contract_info.json'):
#     with open(path) as f:
#         info = json.load(f)
#     return info['abi'], info['address']

# # Connect to local Ganache (or testnet)
# def connect_to_blockchain():
#     web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Update if using a different port/provider
#     if not web3.is_connected():
#         raise ConnectionError("Failed to connect to the blockchain.")
#     return web3


# # Fetch health data from IPFS using CID from contract
# def fetch_health_data(contract):
#     records = contract.functions.getRecords().call()
#     health_data = []

#     for record in records:
#         cid = record[8]  # index of 'cid' in Record struct
#         ipfs_url = f"https://ipfs.io/ipfs/{cid}"
#         print(f"Fetching from IPFS: {ipfs_url}")
#         try:
#             response = requests.get(ipfs_url)
#             data = response.json()
#             health_data.append(data)
#         except Exception as e:
#             print(f"Failed to fetch {cid}: {e}")

#     return health_data

# def main():
#     abi, address = load_contract_info()
#     web3 = connect_to_blockchain()
#     contract = web3.eth.contract(address=address, abi=abi)

#     # Fetch health data from blockchain → IPFS
#     data = fetch_health_data(contract)

#     if not data:
#         print("No health data found. Exiting.")
#         return

#     # Train and test the ML model
#     model = train_ml_model(data)

#     # Visualize (optional)
#     visualize_data(data, model)

# if __name__ == '__main__':
#     main()




