# Most Frequent Element
nums=[1,2,3,1,2,3,3,3,3,3,3,3,3,5]
check={}
for i in nums:
  if i not in check:
    check[i]=1
  else:
    check[i]+=1
print(check)

large=0
for i in check:
  if check[i]>large:
    large=check[i]
    name=i
print(f"{name} : {large}")

#or 
print(max(check, key=check.get))

#or

lis = [1,2,2,3,3,3,3,4,3,3,3,3,3,3,3,4,5,5,5,5,5]
c=0
for i in lis:
  if lis.count(i)>c:
    c=lis.count(i)
    f=i
print(f"{f}:{c}")

