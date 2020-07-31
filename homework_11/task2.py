def meat():
    return 'Meat'

def bread(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print('Bread')
    return inner

def mayonnaise(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print('Mayonnaise')
    return inner

def ketchup(func):
    def inner(*args, **kwargs):
        print('Ketchup')
        func(*args, **kwargs)
    return inner

def salad(func):
    def inner(*args, **kwargs):
        print('Salad')
        func(*args, **kwargs)
    return inner

def tomato(func):
    def inner(*args, **kwargs):
        print('Tomato')
        func(*args, **kwargs)
    return inner

while True:
    try:
        choice = int(input('Choose a sandwich "1-5" '))
        if choice == 1:
            @bread

            def printer(msg):
                print(msg)
            printer(meat())
            print("*" * 50)
            
        elif choice == 2:

            @bread
            @mayonnaise

            def printer(msg):
                print(msg)
            printer(meat())
            print("*" * 50)
            
        elif choice == 3:

            @bread
            @mayonnaise
            @ketchup

            def printer(msg):
                print(msg)
            printer(meat())
            print("*" * 50)

        elif choice == 4:

            @bread
            @mayonnaise
            @salad
            @ketchup

            def printer(msg):
                print(msg)
            printer(meat())
            print("*" * 50)
            
        elif choice == 5:

            @bread
            @mayonnaise
            @tomato
            @salad
            @ketchup

            def printer(msg):
                print(msg)
            printer(meat())
            print("*" * 50)
        
        else:
            print("We need time to come up with new sandwiches!")
            break
    except ValueError:
        print("Enter a number")
    except Exception:
        print('You did a mistake')