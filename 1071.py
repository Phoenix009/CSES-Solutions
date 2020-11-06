for t in range(int(input())):
	x, y = map(int, input().split())
	ans = (max(x, y) - 1)**2
	if ans % 2:
		ans += x
		if y < x:
			ans += x - y
	else:
		ans += y
		if x < y:
			ans += y - x
	print(ans)
