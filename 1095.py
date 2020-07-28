MOD = 10**9 + 7

def fastPower(a, b, mod):
    ans = 1
    a %= mod
    while b:
        if b&1:
            ans *= a
        a = ((a % mod)*(a % mod) % mod)
        ans %= mod
        b >>= 1
    return ans



for t in range(int(input())):
    a, b = map(int, input().split())
    print(fastPower(a, b, MOD))
