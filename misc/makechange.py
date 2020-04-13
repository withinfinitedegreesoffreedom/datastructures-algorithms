
def change_maker(amount, denoms, index, memo):
    if (amount, index) in memo.keys():
        return memo[(amount, index)]
    if index == len(denoms) - 1:
        return 1

    ways = 0
    demon_amt = denoms[index]
    i = 0
    while (i*demon_amt) <= amount:
        amt_rem = (amount - (i*demon_amt))
        ways += change_maker(amt_rem, denoms, index+1, memo)
        i += 1

    memo[(amount, index)]=ways
    return ways 

def coins(amount, memo):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif memo[amount]:
        return memo[amount]
    else:
        memo[amount] = coins(amount-1, memo) + coins(amount-2, memo) + coins(amount-3, memo) + coins(amount-4, memo)
        return memo[amount]


denoms = [1,2,3,4]
amount = 4
index = 0
memo = dict()
print(change_maker(amount, denoms, index, memo))
memo = [None]*(amount+1)
print(coins(amount, memo))

def coin_change(amount, denoms, memo):
    if  amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif memo[amount]:
        return memo[amount]
    else:
        ways = 0
        for i in range(0,len(denoms)):
            #if denoms[i] <= amount:
            ways += coin_change(amount-denoms[i],denoms,memo)
        memo[amount] = ways
        return memo[amount]

memo = [None]*(amount+1)
denoms = [1,2,3,4]
amount = 4
print(coin_change(amount, denoms, memo))