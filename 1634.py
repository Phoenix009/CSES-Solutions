def getAns(coins, amount):
    if amount == 0:
        return 0
    change = {}
    wait = []
    for i in coins:
        if i == amount:
            return 1
        if i < amount:
            wait.append(i)
            change[i] = 1
    
    while(wait):
        newWait = []
        for i in wait:
            for j in coins:
                if i+j == amount:
                    return change[i] + 1
                if i+j < amount and i+j not in change:
                    change[i+j] = change[i]+1
                    newWait.append(i+j)
        wait = newWait
    return -1
 
 
 
n, x = map(int, input().split())
coins = list(map(int, input().split()))
ans = getAns(coins, x)
print(ans)