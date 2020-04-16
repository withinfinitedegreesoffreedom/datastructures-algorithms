
def combination_sum(candidates, target):
    if candidates is None:
        return []

    answer=set()
    for i, candidate in enumerate(candidates):
        for j, num in enumerate(candidates):
            elems = [candidate]
            add = sum(elems)
            while add < target:
                add += num
                elems.append(num)
            if add == target:
                answer.add(tuple(sorted(elems)))
    return [list(item) for item in answer]

#candidates=[2,3,6,7]
#target=7
#candidates=[2,3,5]
#target=8
candidates=[7,3,2]
target=18
print(combination_sum(candidates, target))


