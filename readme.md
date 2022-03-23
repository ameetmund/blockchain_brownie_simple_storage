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