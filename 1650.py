from math import ceil, log2
MAX = 0

def build(arr, segTree, lo, hi, idx):
    if lo == hi:
        segTree[idx] = arr[lo]
    else:
        mid = lo + (hi-lo)//2
        build(arr, segTree, lo, mid, 2*idx+1)
        build(arr, segTree, mid+1, hi, 2*idx+2)
        segTree[idx] = segTree[2*idx+1] ^ segTree[2*idx+2]


def query(segTree, lo, hi, l, r, idx):
    if lo > r or hi < l:
        return MAX
    elif l <= lo and hi <= r:
        return segTree[idx]
    else:
        mid = lo + (hi-lo)//2
        left = query(segTree, lo, mid, l, r, 2*idx +1)
        right = query(segTree, mid+1, hi, l, r, 2*idx +2)
        return left ^ right

n, q = map(int, input().split())
arr = list(map(int, input().split()))
power = ceil(log2(n)) + 1
length = 2**power
segTree = [None for i in range(length)]
build(arr, segTree, 0, n-1, 0)

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ans = query(segTree, 0, n-1, l, r, 0)
    print(ans)
