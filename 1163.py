# r-l

x, n = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
passages = [(0, x)]
for i in range(n):
    newPassage = []
    bestLength = 0
    mid = arr[i]

    for passage in passages:
        l, r = passage
        if l <= mid <= r :
            left = mid - l
            right = r - mid
            if left > right:
                if left == bestLength:
                    newPassage.append((l, mid))
                elif left > bestLength:
                    newPassage = [(l, mid)]
                    bestLength = left
            elif right > left:
                if right == bestLength:
                    newPassage.append((mid, r))
                else:
                    bestLength = right
                    newPassage = [(mid, r)]
            else:
                if left == bestLength:
                    newPassage.append((l, mid))
                    newPassage.append(mid, r)
                elif left > bestLength:
                    bestLength = left
                    newPassage = [
                        (l, mid),
                        (mid, r)
                    ]
        else:
            length = r - l
            if length == bestLength:
                newPassage.append((l, r))
            elif length > bestLength:
                bestLength = r-l
                newPassage = [(l, r)]


    ans.append(bestLength)
    passages = newPassage

print(*ans)
