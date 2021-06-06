def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si],a[si+c]=a[si+c],a[si]
    index=si+c
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return index






def quicksort(a,si,ei):
    if si>ei:
        return
    i=partition(a,si,ei)
    quicksort(a,si,i-1)
    quicksort(a,i+1,ei)


l=[2,4,5,1]
quicksort(l,0,len(l)-1)
print(l)