# Remove duplicate values:

d = {"a":1, "b":2, "c":1, "d":3}
d1={}
temp=[]
for i in d:
  if i not in temp: # if the key is not in temp
    if d[i] not in temp: # if the value is not in temp
      temp.append(d[i]) #appending the value in temp so that it can filter out the duplicates
      d1[i]=d[i] # assigning the values to their keys in a blank dic
print(d1)
