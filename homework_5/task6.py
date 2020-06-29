a = input("Enter a text ")

print('Uppercase availability: ', any(s.isupper() for s in a))
print('Lowercase availability: ', any(s.islower() for s in a))