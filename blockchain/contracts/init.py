from importlib import import_module
from typing import List

__all__: List[str] = []

def register_contract(contract_name: str) -> None:
    """Register a contract in the contracts module."""
    contract = import_module(f"blockchain.contracts.{contract_name}")
    __all__.append(contract_name)

register_contract("NexauraContract")
