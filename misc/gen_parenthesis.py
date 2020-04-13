def gen_parens(n):
    if n == 1:
        return ['()']
    results =  []
    prev_sols = gen_parens(n-1)
    for sol in prev_sols:
        for i in range(0,len(sol)):
            new_sol = sol[:i] + '()' + sol[i:]
            if new_sol not in results:
                results.append(new_sol)
    return results

print(gen_parens(4))

# doesn't  work
def gen_parens_1(results, s, leftrem, rightrem, count):
    if leftrem < 0 or leftrem > rightrem:
        return results
    if rightrem == 0 and leftrem == 0:
        results.append(s)
        return results
    elif leftrem > 0:
        s += "("
        gen_parens_1(results, s, leftrem-1, rightrem, count+1)
    elif leftrem < rightrem:
        s += ")"
        gen_parens_1(results, s, leftrem, rightrem-1, count+1)
    return results

n = 3
s = ""
count = 0
leftrem = n
rightrem = n
print(gen_parens_1([], s, leftrem, rightrem, count))
 
