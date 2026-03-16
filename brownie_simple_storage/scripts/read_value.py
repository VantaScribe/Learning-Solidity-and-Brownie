from brownie import accounts, config
from brownie import Tutorial


def read_contract():
    tutorial_storage = Tutorial[-1]
    
    # -1 for every new script.
    # brownie automically knows ABI and Address 
    print (tutorial_storage.retrieve())





def main():
    read_contract()