# Group words by first letter:
words = ["apple","ant","banana","bat","cat"]
d={}
for i in words:
  lower=i.lower()
  if lower not in d:
    if lower[0] not in d:
      d[lower[0]]=[i] # i works but you need everything in lower use lower instead of i
    else:
      d[lower[0]]+=[i]
print(d)