'''linear search
 TIME COMPLEXITY:BEST:O(1) ,WORST:O(N)'''
item=int(input())
l=[10,23,20,45,89]
for i in l:
    if i==item:
        print("element is found")
        break
else:
        print("element is not found")
        
