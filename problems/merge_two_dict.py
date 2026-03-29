# Merge Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

for i in d1:
  for j in d2:
    if i == j:
      d1[i]+=d2[j]
else:
  d1[j]=d2[j]

print(d1)

#or

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

for i in d2:
  if i in d1:
    d1[i]+=d2[i]
  else:
    d1[i]=d2[i]

print(d1)


