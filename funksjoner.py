def areal_rektangel(length, width):
    return length * width

l = float(input("lengde: "))
b = float(input("bredde: "))

a = areal_rektangel(l, b)
print(f"Arealet av rektangelet er: {a}")