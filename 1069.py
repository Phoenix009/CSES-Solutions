seq = input()
maxCount = 0
count = 1
 
for i in range(1, len(seq)):
    if seq[i] == seq[i-1]:
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 1
maxCount = max(maxCount, count)
 
print(maxCount)
