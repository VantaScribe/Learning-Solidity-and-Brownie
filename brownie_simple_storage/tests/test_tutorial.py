from brownie import accounts, Tutorial

def test_deploy():
    # Arrange 
    account = accounts[0]
    
    # Act
    tutorial_storage = Tutorial.deploy({"from": account})
    starting_value = tutorial_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


    def test_update_storage():
        #Arrange
        account = accounts[0]
        tutorial_storage = Tutorial.deploy({"from": account})
        #Act 
        expected = 20
        tutorial_storage.store(expected, {"from": account})
        
        #Assert
        assert 20 == tutorial_storage.retrieve()

