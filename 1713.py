from math import ceil


def getDivisors(n):
    facts = {}
    ct = 0
    while n %2 == 0:
        n //= 2
        ct += 1
    facts[2] = ct

    i = 3
    while i <= ceil(n**0.5) and n > 1:
        ct = 0
        while n % i == 0:
            n //= i
            ct += 1

        if ct:
            facts[i] = ct
        i += 1

    if n > 1:
        facts[n] = 1

    return facts





for t in range(int(input())):
    divisors = getDivisors(int(input()))
    ans = 1
    for i in divisors:
        ans *= (divisors[i] + 1)
    print(ans)
