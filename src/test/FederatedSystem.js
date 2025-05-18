import React, { useState, useEffect } from 'react';
import Web3 from 'web3'; // You might need Web3.js to interact with Ethereum
import FederatedAccessControl from "../build/contracts/FederatedAccessControl.json";

// Use the deployed contract address
const deployedAddress = "0x895135D07736c8FEC80897968ec914Fb2CbA6cf1";

const FederatedSystem = () => {
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);

  useEffect(() => {
    const initialize = async () => {
      const web3 = new Web3(window.ethereum); // Connecting to Ethereum browser extension (e.g., MetaMask)
      await window.ethereum.enable(); // Request access to the user's Ethereum account

      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]); // Set the first account

      const networkId = await web3.eth.net.getId();
      const contractNetwork = FederatedAccessControl.networks[networkId];
      if (contractNetwork) {
        const contractInstance = new web3.eth.Contract(
          FederatedAccessControl.abi,
          deployedAddress
        );
        setContract(contractInstance);
      } else {
        console.error('Contract not deployed to the detected network.');
      }
    };

    initialize();
  }, []);

  return (
    <div className="federated-system">
      <h1>Federated System</h1>
      <p>Account: {account}</p>
      {/* Add UI elements to interact with the contract */}
    </div>
  );
};

export default FederatedSystem;
