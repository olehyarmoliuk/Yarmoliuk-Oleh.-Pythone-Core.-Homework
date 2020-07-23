while True:
    try:
        listLength = int(input('How many elements do you want to add to the tuple? '))
        listTuple = ([], [], [])

        list_tuple_1 = tuple([input('Enter a letter, a digit, or a special symbol ') for i in range(listLength)])

        print(list_tuple_1)

        for symb in list_tuple_1:
            elem = ord(symb[0])
            if 47 < elem < 58:
                symb = int(symb)
                listTuple[0].insert(0, symb)
            elif 96 < elem < 123 or 64 < elem < 91:
                listTuple[1].insert(1, symb)
            else:
                listTuple[2].insert(2, symb) 
        print(listTuple)
        break

    except ValueError:
        print('Enter a digit!')