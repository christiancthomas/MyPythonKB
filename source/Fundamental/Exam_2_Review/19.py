sum = 0
for i in range(1,31):
    print(f"{i}/{31-i} +")
    sum += i / (31-i)
print(f"final sum: {sum}")