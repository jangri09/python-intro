spill = []

for i in range(5):
    s = input(f"Skriv inn favorittspillet #{i+1}: ")
    spill.append(s)

print("Dine favorittspill er:")
for i in range(len(spill)):
    print(f"{i+1}. {spill[i]}")