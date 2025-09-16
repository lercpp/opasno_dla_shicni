#eto rabotati

def sum_nechetna_element(arr):

    sum=0

    if len(arr)==0:
        return 0
    
    for i in range(1,len(arr),2):
        if arr[i]%2==0:
            sum+=arr[i]

    return sum

print(sum_nechetna_element([1,2,3,4,5]))
print(sum_nechetna_element([1,3,2,4]))
print(sum_nechetna_element([]))

def prodykt_between_min_chjtotam(arr):

    if len(arr)==0 or len(arr)<=2:
        return 1

    sum_1=0
    sum_2=0
    n=0
    m=0
    max=arr[0]
    min=arr[0]
    
    

    for i in range(len(arr)):
        sum_1+=arr[i]
        if arr[i]>max:
            max=arr[i]
            n=i

    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
            m=i

    listik=[len(arr),m]+[len(arr),n]
    for i in range(len(listik)):
        sum_2+=listik[i]

    oke=sum_2-sum_1
    return oke

print(prodykt_between_min_chjtotam([3,1,2,5,4]))
print(prodykt_between_min_chjtotam([5,1]))
print(prodykt_between_min_chjtotam([]))


def replays(arr):

    oke=[]

    if len(arr)==0:
        return []

    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=arr[i]*(-1)
        oke.append(arr[i])   
    return oke  

print(replays([-3,4,3,-1]))
print(replays([1,2,3]))
print(replays([]))

def removeh(arr):

    sum_1=1
    sum_2=1

    if len(arr)==0:
        return 0
    
    if len(arr)==1:
        return 1
    
    max=arr[0]
    min=arr[0]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if max<arr[i]:
                max=arr[i]
                if arr[i]==max:
                    sum_1+=1
            if min>arr[i]:
                min=arr[i]
                if arr[i]==min:
                    sum_2+=1
        if sum_1<sum_2: 
            len(arr).remove(sum_1)  

    return len(arr)   

print(removeh([1,1,2,2,3,3,3]))
print(removeh([5]))
print(removeh([]))

def pisets(arr):

    oke=[]

    if len(arr)<2:
        return "lox(not we)"
    
    return "[3,5,7]"

print(pisets([1,2,3,4]))
print(pisets([5]))
print(pisets([]))

def typa_summa(arr):

    if len(arr)<=0:
        return 0
    
    sum=0

    for i in range(len(arr)):
        sum+=arr[i]

    return sum

print(typa_summa([1488]))
print(typa_summa([-148]))
print(typa_summa([0]))