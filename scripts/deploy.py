from brownie import accounts


def deploy_simple_storage():
    # account = accounts[0]  # This is the way to add local ganache account
    account = accounts.load("rinkeby-test")  # This is the way to add testnet accounts
    print(account)


def main():
    deploy_simple_storage()
