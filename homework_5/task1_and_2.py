key = 4 

def encrypt(string, key):


  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter a sentence: ")
print("Original messege is: ", text)
print("Encrypted: ", encrypt(text, key))


def decrypt(string, key):
      

  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - key - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - key - 97) % 26 + 97)
  
  return cipher

decr_text = encrypt(text, key)
print('Text after decryption is: ', decrypt(decr_text, key))