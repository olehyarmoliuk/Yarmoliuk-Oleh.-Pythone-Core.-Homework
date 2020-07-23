tuple_1 = (31, 55, 76, 999, 112, 'abc', 'Hello', 'Pyt', 'hon', '!', '##', '@@$@@')
print(tuple_1)

elem = input('Enter an element to find out its index ')

if elem in tuple_1:
    print(tuple_1.index(elem))
else:  
    try:
        elem = int(elem)
        print(tuple_1.index(elem)) 
    except:
        print('There is no such element in the tuple')
