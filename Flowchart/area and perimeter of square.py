side = int(input("Enter the length of a side: "))
choice = int(input("""1) Get Area
2) Get Perimeter
"""))
if choice == 1:
    output = side**2
elif choice == 2:
    output = side*4
print(output)