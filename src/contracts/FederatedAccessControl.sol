// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FederatedAccessControl {
    // Struct to represent a healthcare provider
    struct Provider {
        string name;
        address providerAddress;
        bool isAuthorized;
    }

    // Mapping to store authorized providers
    mapping(address => Provider) public providers;

    // Address of the contract owner
    address public owner;

    // Events
    event ProviderAdded(address indexed providerAddress, string name);
    event ProviderRemoved(address indexed providerAddress);
    event AccessGranted(address indexed providerAddress);
    event AccessRevoked(address indexed providerAddress);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if a provider is authorized
    modifier onlyAuthorizedProvider() {
        require(providers[msg.sender].isAuthorized, "Not an authorized provider");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // Function to add a new healthcare provider
    function addProvider(address _providerAddress, string memory _name) public onlyOwner {
        require(!providers[_providerAddress].isAuthorized, "Provider already exists");
        providers[_providerAddress] = Provider(_name, _providerAddress, true);
        emit ProviderAdded(_providerAddress, _name);
    }

    // Function to remove a healthcare provider
    function removeProvider(address _providerAddress) public onlyOwner {
        require(providers[_providerAddress].isAuthorized, "Provider does not exist");
        delete providers[_providerAddress];
        emit ProviderRemoved(_providerAddress);
    }

    // Function to grant access to a provider
    function grantAccess(address _providerAddress) public onlyOwner {
        require(providers[_providerAddress].providerAddress != address(0), "Provider does not exist");
        providers[_providerAddress].isAuthorized = true;
        emit AccessGranted(_providerAddress);
    }

    // Function to revoke access from a provider
    function revokeAccess(address _providerAddress) public onlyOwner {
        require(providers[_providerAddress].isAuthorized, "Provider is not authorized");
        providers[_providerAddress].isAuthorized = false;
        emit AccessRevoked(_providerAddress);
    }

    // Function to check if a provider is authorized
    function isAuthorized(address _providerAddress) public view returns (bool) {
        return providers[_providerAddress].isAuthorized;
    }
}