### Implement simple storage using brownie

#### Commands to do initial set up
> _Download pipx_ - 'python3 -m pip install --user pipx'.

> _Download pipx ensurepath_ - 'python3 -m pipx ensurepath --force'. Close and re-opne terminal.

> Run 'pipx install eth-brownie'.

> Run 'sudo apt install python3.8-venv'.

> Run 'pipx install eth-brownie'. Close and re-open terminal.

> Run 'brownie --version' to check if brownie is successfully installed or not.

> Create a new brownie project by typing 'brownie init'. 

#### Project structure
> _build_ - 
>   - _contracts_ - Contains the compiled version of smart contracts.Dont't manually add contracts into this folder.
>   - _deployments_ - Tracks all the deployments across different chains.
>   - _interfaces_ - Any interfaces that we are working with

> _contracts_ - All the smart contracts reside under this.

> _interfaces_ - Stores all the interfaces

> _reports_ - Stores any type of report we want to run.

> _scripts_ - Automate tasks like deploying or calling functions.

> _tests_ - For unit testing.

#### Step by step execution -
> Compile the smart contract by using 'brownie compile'. It will generate a new json object under /build/contracts
> Add a new script 'deploy.py' under /scripts. Run 'brownie run scripts/deploy.py to run the python code. It launches ganache automatically in local mode. So brownie does the compile, create a compiled json object, gets the abi and bytecode and spins up local ganache automatically. 
>   - But we have to get the accounts into the code.  This will be done by having a statement 'from brownie import accounts' at the top and use accounts[] list to get the specific account from local ganache chain.
>   - Another way of adding accounts to brownie is to run it through CLI. We need to run the command 'brownie accounts new account-name' e.g. 'brownie accounts new rinkeby-test'. This will ask you to input the private key from metamask. It will ask you to enter the metamask password. Then the account will be added to brownie. These accounts will be accessed through 'accounts.load("rinkeby-test")' 
