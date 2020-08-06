from collections import Counter
s = input()
frq = Counter(s)
ans = ''
flg = True
special = None

for i in frq:
    if frq[i]%2:
        if not special:
            special = i
        else:
            flg = False
            break
    else:
        ans += i*(frq[i]//2)

if flg:
    if special:
        print(f'{ans}{special*frq[special]}{ans[::-1]}')
    else:
        print(f'{ans}{ans[::-1]}')
else:
    print('NO SOLUTION')