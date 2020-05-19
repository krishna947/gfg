#code
# Time Complexity : O(log(min(n, m))), where n and m are the sizes of given sorted array

from math import floor
def getMedian(arrn, arrm):
    n1,n2 = len(arrn), len(arrm)
    begin1=0
    end1=n1
    while(begin1<=end1):
        i1 = int((begin1+end1)/2)
        i2 = int((n1+n2+1)/2) - i1
        
        min1 = arrn[i1] if i1 != n1 else 10**10
        max1 = arrn[i1-1] if i1 != 0 else -10**10
        min2 = arrm[i2] if i2 != n2 else 10**10
        max2 = arrm[i2-1] if i2 != 0 else -10**10
        
        if max1 <= min2 and max2 <= min1:
            if (n1+n2)%2 == 0:
                return floor((max(max1,max2)+min(min1,min2))/2)
            else:
                return max(max1,max2)
        elif max1 > min2:
            end1 = i1-1
        else:
            begin1 = i1+1
            
    
    
for _ in range(int(input())):
    n,m = map(int, input().split())
    arrn = list(map(int, input().split()))
    arrm = list(map(int, input().split()))
    
    if n <= m: 
        print(getMedian(arrn, arrm))
    else:
        print(getMedian(arrm, arrn))
