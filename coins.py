# Memoization
def coins(n):
	memo_arr = [None]*(n+1)
	return find_ways(n, memo_arr)

def find_ways(n, memo):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif memo[n]:
		return memo[n]
	else:
		memo[n] = find_ways(n-1, memo) + find_ways(n-5, memo) + find_ways(n-10, memo) + find_ways (n-25, memo)
		return memo[n]


if __name__ == '__main__':
  print(coins(4))