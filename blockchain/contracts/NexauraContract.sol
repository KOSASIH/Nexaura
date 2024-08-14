pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract NexauraContract {
    using SafeERC20 for address;
    using SafeMath for uint256;

    // Mapping of user addresses to their balances
    mapping (address => uint256) public balances;

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawal(address indexed user, uint256 amount);

    // Function to deposit tokens
    function deposit(uint256 amount) public {
        balances[msg.sender] = balances[msg.sender].add(amount);
        emit Deposit(msg.sender, amount);
    }

    // Function to withdraw tokens
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(amount);
        emit Withdrawal(msg.sender, amount);
    }
}
