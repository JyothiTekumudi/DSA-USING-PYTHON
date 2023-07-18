print("enter the list elements:")
l=list(map(int,input().split()))
low=0
high=len(l)-1
mid=0
print("------If given list is not in sorted order than sort it or if it is in sorted leave it-------")
l.sort()
print("printing the sorted list:")
print(l)
print("Give the element which need to be search:")
key=int(input())
while low<=high:
    mid=(low+high)//2
    if l[mid]==key:
        print(key,"element is found at position in",mid)
        break
    elif l[mid]>key:
        high=mid-1
    else:
        low=mid+1
else:
    print("given key is not found")
        
    
