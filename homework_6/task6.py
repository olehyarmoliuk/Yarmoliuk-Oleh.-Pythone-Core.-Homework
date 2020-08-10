# I have no idea how to make it looks better

while True:
    try:
        mtrx_1 = [[int(input("Fill the first matrix in: ")) for i in range(3)] for i in range(3)]
        mtrx_2 = [[int(input("Fill the second matrix in: ")) for i in range(3)] for i in range(3)]
    except ValueError:
        print('Incorrect value!')

mtrx_3 = [[], [], []]


if mtrx_1[0][0] >=  mtrx_2[0][0]:
    mtrx_3[0].insert(0, mtrx_1[0][0])
else:
    mtrx_3[0].insert(0, mtrx_2[0][0])
if mtrx_1[0][1] >=  mtrx_2[0][1]:
    mtrx_3[0].insert(0, mtrx_1[0][1])
else:
    mtrx_3[0].insert(0, mtrx_2[0][1])
if mtrx_1[0][2] >=  mtrx_2[0][2]:
    mtrx_3[0].insert(0, mtrx_1[0][2])
else:
    mtrx_3[0].insert(0, mtrx_2[0][2])
if mtrx_1[1][0] >=  mtrx_2[1][0]:
    mtrx_3[1].insert(1, mtrx_1[1][0])
else:
    mtrx_3[1].insert(1, mtrx_2[1][0])
if mtrx_1[1][1] >=  mtrx_2[1][1]:
        mtrx_3[1].insert(1, mtrx_1[1][1])
else:
    mtrx_3[1].insert(1, mtrx_2[1][1])
if mtrx_1[1][2] >=  mtrx_2[1][2]:
    mtrx_3[1].insert(1, mtrx_1[1][2])
else:
    mtrx_3[1].insert(1, mtrx_2[1][2])
if mtrx_1[2][0] >=  mtrx_2[2][0]:
    mtrx_3[2].insert(2, mtrx_1[2][0])
else:
    mtrx_3[2].insert(2, mtrx_2[2][0])
if mtrx_1[2][1] >=  mtrx_2[2][1]:
    mtrx_3[2].insert(2, mtrx_1[2][1])
else:
    mtrx_3[2].insert(2, mtrx_2[2][1])
if mtrx_1[2][2] >=  mtrx_2[2][2]:
    mtrx_3[2].insert(2, mtrx_1[2][2])
else:
    mtrx_3[2].insert(2, mtrx_2[2][2])

print(mtrx_1)
print(mtrx_2)
print(mtrx_3)