# Complete the triplets function below.
def triplets(a, b, c):
    r=dict()
    q=dict()
    p=dict()
    for i in b:
        if i in q:
            q[i]+=1
        else:
            q[i]=1
    for i in a:
        if i > max(q.keys()):
            pass
        else:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
    for i in c:
        if i > max(q.keys()):
            pass
        else:
            if i in r:
                r[i]+=1
            else:
                r[i]=1

    poss_triplets=[]
    for key in p.keys():
        poss_triplets.append([key,None,None])
    new_triplets=[]
    for i in range(0, len(poss_triplets)):
        for key in q.keys():
            if key >= poss_triplets[i][0]:
                new_triple=poss_triplets[i]
                new_triple[1]=key
                new_triplets.append(new_triple)
    triples=[]
    for triplet in new_triplets:
        for key in r.keys():
            if key <= triplet[1]:
                triplet[2]=key
                triples.append(triplet)
    return triples


a=[1,3]
b=[2,3]
c=[1,2,3]
print(triplets(a,b,c))