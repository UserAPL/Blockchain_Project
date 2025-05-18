const PatientRegistry = artifacts.require("PatientRegistration");
module.exports = function(deployer) {
  deployer.deploy(PatientRegistry);
};

const FederatedAccessControl = artifacts.require("FederatedAccessControl");

module.exports = function (deployer) {
  deployer.deploy(FederatedAccessControl);
};
