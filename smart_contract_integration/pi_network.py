import json
from web3 import Web3, HTTPProvider
from web3.contract import Contract

class PINetworkContract:
    def __init__(self, contract_address, abi, provider_url):
        self.contract_address = contract_address
        self.abi = abi
        self.provider_url = provider_url
        self.w3 = Web3(HTTPProvider(self.provider_url))
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)

    def get_balance(self, address):
        return self.contract.functions.balanceOf(address).call()

    def transfer_tokens(self, sender, recipient, amount):
        tx_hash = self.contract.functions.transfer(recipient, amount).transact({'from': sender})
        return tx_hash

    def get_token_name(self):
        return self.contract.functions.name().call()

    def get_token_symbol(self):
        return self.contract.functions.symbol().call()

    def get_token_decimals(self):
        return self.contract.functions.decimals().call()

    def get_token_total_supply(self):
        return self.contract.functions.totalSupply().call()

# Example usage:
contract_address = '0x...your_contract_address...'
abi = json.load(open('pi_network_abi.json'))
provider_url = 'https://mainnet.infura.io/v3/...your_project_id...'

pi_network_contract = PINetworkContract(contract_address, abi, provider_url)

print(pi_network_contract.get_balance('0x...your_address...'))
print(pi_network_contract.transfer_tokens('0x...sender_address...', '0x...recipient_address...', 100))
print(pi_network_contract.get_token_name())
print(pi_network_contract.get_token_symbol())
print(pi_network_contract.get_token_decimals())
print(pi_network_contract.get_token_total_supply())
