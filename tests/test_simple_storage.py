from brownie import accounts, SimpleStorage


def test_deploy():
    # Arrange the information
    account = accounts[0]

    # Act on the information arranged
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


def test_update():
    # Arrange the information
    account = accounts[0]

    # Act on the information arranged
    simple_storage = SimpleStorage.deploy({"from": account})
    expected_updated_value = 7
    simple_storage.store(7, {"from": account}).wait(1)
    updated_value = simple_storage.retrieve()
    print("expected", expected_updated_value)
    print("retrieved", updated_value)

    # Assert
    assert updated_value == expected_updated_value
