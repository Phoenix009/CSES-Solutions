from math import ceil, log2
MAX = 0

def build(arr, segTree, lo, hi, idx):
    if lo == hi:
        segTree[idx] = arr[lo]
    else:
        mid = lo + (hi-lo)//2
        build(arr, segTree, lo, mid, 2*idx+1)
        build(arr, segTree, mid+1, hi, 2*idx+2)
        segTree[idx] = segTree[2*idx+1] + segTree[2*idx+2]


def query(segTree, lo, hi, l, r, idx):
    if lo > r or hi < l:
        return MAX
    elif l <= lo and hi <= r:
        return segTree[idx]
    else:
        mid = lo + (hi-lo)//2
        left = query(segTree, lo, mid, l, r, 2*idx +1)
        right = query(segTree, mid+1, hi, l, r, 2*idx +2)
        return left + right
        
def update(segTree, lo, hi, idx, uidx, newValue):
    if lo == hi:
        segTree[idx] = newValue
    else:
        mid = lo + (hi-lo)//2
        if lo <= idx <= mid:
            update(segTree, lo, mid, 2*idx+1, uidx, newValue)
        else:
            update(segTree, mid+1, hi, 2*idx+2, uidx, newValue)

        segTree[idx] = segTree[2*idx+1] + segTree[2*idx+2]



n, q = map(int, input().split())
arr = list(map(int, input().split()))
power = ceil(log2(n)) + 1
length = 2**power
segTree = [None for i in range(length)]
build([0 for i in range(n)], segTree, 0, n-1, 0)

for i in range(q):
    k = list(map(int, input().split()))
    if len(k) == 2:
        print(arr[k[1]-1] + query(segTree, 0, n-1, k[1]-1, k[1]-1, 0))
    else:
        update(segTree, 0, n-1, 0, k[1]-1, k[3])
        update(segTree, 0, n-1, 0, k[2], -k[3])