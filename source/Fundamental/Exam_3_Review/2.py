"""Create  a list,  dlist,  which consist  initially  of ten  values 
that are all 3.14. Try  to avoid typing 3.14 ten times.
"""

dlist = []
for _ in range(10):
    dlist.append(3.14)

print(dlist)

# Alternative solution
dlist = [3.14] * 10