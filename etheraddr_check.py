def ethereum_addr_check(ethaddr):
    print ethaddr
    if len(ethaddr) == 42:
        if ethaddr[:2] != '0x':
            return False
        ethaddrhex = ethaddr[2:]
    else:
        if len(ethaddr) != 40:
            return False
        else:
            ethaddrhex = ethaddr

    for c in ethaddrhex:
        if c not in '0123456789ABCDEFabcdef':
            return False

    return True

"""
print ethereum_addr_check('0x5aAeb6053F3E94C9b9AZ9f33669435E7Ef1BeAed')
print ethereum_addr_check('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d3')
print ethereum_addr_check('0xdbF03B407c01E7cD3CBea99509d93f8DDDC6FB')
print ethereum_addr_check('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb')
"""