p = int(input("Enter number of place "))

while p not in range(1, 55):
    print('There is no such place')
    p = int(input("Please enter number of place again "))
    continue


if p in range(1, 37):
    print("Compartment")
else: 
    p in range(37, 55)
    print("Side")

if p in range (1, 54, 2):
    print("Bottom")
else: 
    p in range (2, 55, 2)
    print("Top")

if p in range (1, 5) and (53, 55):
    print("Near conductor")
else:
    p in range (33, 37) and (37, 39)
    print("Near toilet")