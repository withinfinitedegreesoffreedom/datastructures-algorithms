def whatFlavors(cost, money):
    d={}
    n=len(cost)
    for i in range(0,n):
        if cost[i] < money:
            if cost[i] in d:
                d[cost[i]].append(i)
            else:
                d[cost[i]]=[i]
    for key,val in d.items():
        if money-key in d:
            if money-key==key and len(val)>1:
                return ' '.join(map(str,[val[0]+1,d[money-key][1]+1]))
            elif money-key!=key:
                return ' '.join(map(str,[val[0]+1,d[money-key][0]+1]))
        

cost=[7,2,5,4,11]
money=12
print(whatFlavors(cost,money))