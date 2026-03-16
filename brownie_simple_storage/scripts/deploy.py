from brownie import accounts, config, network
from brownie import Tutorial

def deploy_simple_storage():
    account = get_account()
    tutorial_storage = Tutorial.deploy({"from": accounts})
    stored_value = tutorial_storage.retrieve()
    print (stored_value)
    transaction = tutorial_storage.store(20, {"from": accounts})
    transaction.wait(1)
    updated_stored_value = tutorial_storage.retrieve()
    print (updated_stored_value)
    #account = accounts.load("vanebuilds_")
    #print (account)
    #account = accounts.add(config["wallets"]["from_key"])
    #print (account)
def get_account():
    if network.show_active == "development":
        return accounts[0] 
    else:
        return accounts.add(config["wallets"]["from_key"])
def main():
    deploy_simple_storage()
