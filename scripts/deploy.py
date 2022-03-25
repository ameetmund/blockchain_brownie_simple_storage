from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    account = get_account()
    # account = accounts[0]  # This is the way to add local ganache account
    # account = accounts.load("rinkeby-test")  # This is the way to add testnet accounts
    # account = accounts.add(
    #     os.getenv("PRIVATE_KEY")
    # )  # This is the way to add accounts through env variables
    # account = accounts.add(
    #     config["wallets"]["from_key"]
    # )  # This is the way to add env variables without os

    # Deploy SimpleStorage contract. We can notice that it's very simple compared to a
    # longer process of Build --> Sign --> Send Transaction. Those are automatically
    # taken care by brownie.
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print("Available stored value:", stored_value)
    update_value = simple_storage.store(15, {"from": account})
    update_value.wait(1)  # Wait for 1 block for transaction to complete
    print("New value updated in the chain")
    new_stored_value = simple_storage.retrieve()
    print("New value in the chain is", new_stored_value)


# Check if network is development or testnet
def get_account():
    if network.show_active() == "development":
        print("Ganache Development network is used- Version 3")
        return accounts[0]
    else:
        print("Rinkeby testnet is used - Version 3")
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
