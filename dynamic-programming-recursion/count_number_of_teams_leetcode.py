'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5 '''


def count_number_of_teams(rating):
    if rating is None:
        return None

    lesser=[0]*len(rating)
    greater=[0]*len(rating)
    ans=0

    for i in range(0, len(rating)-1):
        for j in range(i+1, len(rating)):
            if rating[i]>rating[j]:
                lesser[i]+=1
            elif rating[i]<rating[j]:
                greater[i]+=1
    for i in range(0, len(rating)-1):
        for j in range(i+1, len(rating)):
            if rating[i]>rating[j]:
                ans+=lesser[j]
            elif rating[i]<rating[j]:
                ans+=greater[j]
    return ans

rating=[2,5,3,4,1]
print(count_number_of_teams(rating))
rating=[1,5,4,3,0,6,8,7]
print(count_number_of_teams(rating))