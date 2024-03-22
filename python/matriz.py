M = []
for i in range(0,3):
  M.append([])
  for j in range(0,3):
    if i==j:
      M[i].append(1)
    else:
      M[i].append(0)

print(M)
