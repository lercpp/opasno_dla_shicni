def sum_nechetna_element(arr):

    if len(arr)==0:
        return None
    
    for i in range(1,len(arr),2):
        if arr[i]%2==0:
            sum+=arr[i]

    return sum


def prodykt_between_min_chjtotam(arr):

    sum_1=0
    sum_2=0
    n=0
    m=0

    if len(arr)==0 or len(arr)<=2:
        return 1
    
    else:
        for i in range(len(arr)):
            sum_1+=arr[i]
            if arr[i]>max:
                max=arr[i]
                n=i

        for i in range(len(arr)):
            if arr[i]<min:
                min=arr[i]
                m=i

    listik=[len(arr),m]+[len[arr],n]
    for i in listik:
        sum_2+=listik[i]

    oke=sum_2-sum_1
    return oke

def replays(arr):

    oke=[]

    if len(arr)==0:
        return None

    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=arr[i]*(-1)
        oke.apend(arr[i])   
    return oke  

def remove(arr):

    sum_1=1
    sum_2=1

    if len(arr)==0:
        return None
    
    if len(arr)==1:
        return 1

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
        if sum_1<sum_2 or sum_2<sum_1:
            len(arr).remove(sum_1 or sum_2)  

    return len(arr)   

def sum_local(arr):

    max_1=arr[0]
    n=0

    if len(arr)<=2:
        return None
    
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i]
            n=i

    len(arr).remove(arr[n])

    for i in range(len(arr)):
        if max_1<arr[i]:
            max_1=arr[i]

    return max,max_1

def pisets(arr):

    oke=[]

    if len(arr)<2:
        return None
    
    for i in range(len(arr)):
        for j in range(2,len(arr)):
            sum+=arr[i]+arr[j]
            oke.append(sum)
    return oke

def typa_summa(arr):

    if len(arr)>=0:
        return None
    
    for i in range(len(arr)):
        sum+=arr[i]

    return sum