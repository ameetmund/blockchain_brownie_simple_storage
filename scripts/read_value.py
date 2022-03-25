from brownie import SimpleStorage


def read_contracts():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contracts()
