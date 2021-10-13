#monoalphabetic encryption is defined
def Option1():
    print("This is the monoalphabetic encryption")

    #random function
    import random

    #opens textfile
    text_file = open("MonoalphabeticEncryptionTextfile.txt" , "r")

    #splits alphabet into a list
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters =  []

    for i in range(0, len(letters)):
        characters.append(chr(i+97))

    #reads textfile
    #puts textfile into a list to be encrypted
    original_file = text_file.read()
    message = []

    for i in range(0, len(original_file)):
        message.append(original_file[i])
        
    encrypted = []
    result = ""
    code = ""

    #generates key
    key = random.randint(1, 24)

    #encrypts textfile
    for i in range(0, len(message)):
        
        #uses ASCII to convert letters to numbers
        new_message = ord(message[i])

        #ensures spaces aren't encrypted
        if new_message != 32:
            result = new_message - key
        elif new_message == 32:
            result = 32

        #start and end of alphabet    
        if result < 97:
            result = new_message + (26 - key)
        elif result > 122:
            result = new_message - (26 - key)
        code = chr(result)
        encrypted.append(code)
        result = ""
        code = ""


    #turn encrypted array into string
    encryptedString = ""
    for i in range(0,len(encrypted)):
        encryptedString += encrypted[i]

    print(encryptedString)
    
    text_file.close()

    #user can return to menu or exit program
    print("Return to menu? Y/N")
    Return = input()
    if Return == 'Y':
        return menu()
    elif Return == 'N':
        quit()

#polyalphabetic encryption is defined
def Option2():
    print("This is the polyalphabetic encryption (new key for each letter)")

    #random function
    import random

    #opens textfile
    text_file = open("PolyalphabeticEncryptionTextfile.txt" , "r")

    #splits alphabet into a list
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters =  []

    for i in range(0, len(letters)):
        characters.append(chr(i+97))

    #reads textfile
    #puts textfile into a list to be encrypted
    original_file = text_file.read()
    message = []

    for i in range(0, len(original_file)):
        message.append(original_file[i])
        
    encrypted = []
    result = ""
    code = ""

    #encrypts textfile
    for i in range(0, len(message)):

        #generates key
        key = random.randint(1, 24)
        
        #uses ASCII to convert letters to numbers
        new_message = ord(message[i])

        #ensures spaces aren't encrypted
        if new_message != 32:
            result = new_message - key
        elif new_message == 32:
            result = 32

        #start and end of alphabet    
        if result < 97:
            result = new_message + (26 - key)
        elif result > 122:
            result = new_message - (26 - key)
        code = chr(result)
        encrypted.append(code)
        result = ""
        code = ""

    #turn encrypted array into string
    encryptedString = ""
    for i in range(0,len(encrypted)):
        encryptedString += encrypted[i]

    print(encryptedString)

    text_file.close()

    #user can return to menu or exit program
    print("Return to menu? Y/N")
    Return = input()
    if Return == 'Y':
        return menu()
    elif Return == 'N':
        quit()



#polyalphabetic double cipher encryption is defined
def Option3():
    print("This is the polyalphabetic encryption (double cipher)")
    #this is to have two different caesar ciphers at the same time (one for odd numbers the other for even)
    def two_ceaser_ciphers():
    #input the message from the user one letter at a time or it will be harder to 
      print("How many letters (without spaces) are in your program?")
      Number_of_Letters = int(input())
      #2 different letters at a time so the amount of times will be divided by two
      if (Number_of_Letters % 2) == 0:
        TimesToGoThrough = int(Number_of_Letters/2)

        print("Please do not include spaces when typing your message.")
        for i in range(0,TimesToGoThrough):
            #Do first cipher
            print("Please enter your next letter")
            CipherOne = str(input())
            alpha = []
            alpha.append(CipherOne)
            result = ""
            new_message = ord(CipherOne)
            EncodedCipherOne = chr(new_message + 3)
            print(EncodedCipherOne)
            #Encode second cipher
            print("Please enter your next letter")
            CipherTwo = str(input())
            alpha2 = []
            alpha2.append(CipherTwo)
            result = ""
            new_message2 = ord(CipherTwo)
            EncodedCipherTwo = chr(new_message2 + 5)
            EncodedMessage = [EncodedCipherOne, EncodedCipherTwo]
            print(EncodedCipherTwo)
      elif (Number_of_Letters % 2) == 1:
          TimesToGoThrough = int(Number_of_Letters/2)

          print("Please do not include spaces when typing your message.")
          for i in range(0,TimesToGoThrough):
              #Do first cipher
              print("Please enter your next letter")
              CipherOne = str(input())
              alpha = []
              alpha.append(CipherOne)
              result = ""
              new_message = ord(CipherOne)
              EncodedCipherOne = chr(new_message + 3)
              print(EncodedCipherOne)
              #Encode second cipher
              print("Please enter your next letter")
              CipherTwo = str(input())
              alpha2 = []
              alpha2.append(CipherTwo)
              result = ""
              new_message2 = ord(CipherTwo)
              EncodedCipherTwo = chr(new_message2 + 5)
              print(EncodedCipherTwo)  
          #Do first cipher one extra time
          print("Please enter your next letter")
          CipherOne = str(input())
          alpha = []
          alpha.append(CipherOne)
          new_message = ord(CipherOne)
          EncodedCipherOne = chr(new_message + 3)
          print(EncodedCipherOne)        

    two_ceaser_ciphers()

    #user can return to menu or exit program
    print("Return to menu? Y/N")
    Return = input()
    if Return == 'Y':
        return menu()
    elif Return == 'N':
        quit()


#monoalphabetic brute force decryption is defined
def Option4():
    print("This is the monoalphabetic decryption")

    #opens textfile
    text_file = open("MonoalphabeticDecryptionTextfile.txt", "r+")

    #splits alphabet into a list
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = []

    for i in range(0, len(letters)):
        characters.append(chr(i+97))

    #reads textfile
    original_file = text_file.read()

    #splits textfile into a list to be encrypted
    message = []
    for i in range(0, len(original_file)):
        message.append(original_file[i])

    #defines variables                          
    decrypted = []
    result = ""
    code = ""

    #brute force decryption(runs through all possible keys)
    for i in range(0, len(characters)):
       
        #generates key for each iteration
        key = i
                
        #decrypts textfile
        for i in range(0, len(message)):
            #uses Unicode to convert letters to numbers
            new_message = ord(message[i])

            #ensures spaces aren't decrypted
            if new_message != 32:
                result = new_message - key
            elif new_message == 32:
                result = 32

            #accommodates start and end of alphabet    
            if result < 97:
                result = new_message + (26 - key)
            elif result > 122:
                result = new_message - (26 - key)

            #saves decrypted letter
            code = chr(result)

            #inserts decrypted letter into final message
            decrypted.append(code)
            
            #resets variables
            result = ""
            code = ""

        #outputs decrypted string from textfile
        #turn encrypted array into string
        decryptedString = ""
        for i in range(0,len(decrypted)):
            decryptedString += decrypted[i]

        print(decryptedString)
        
        #resets variables
        decrypted = []    
        result = ""
        code = ""

    #closes textfile
    text_file.close()

    #user can return to menu or exit program
    print("Return to menu? Y/N")
    Return = input()
    if Return == 'Y':
        return menu()
    elif Return == 'N':
        quit()

#used for option 5
def CreateAnagram(message):

  import random

  #puts message into array
  original = []

  for i in range(0,len(message)):
    original.append(message[i])
    
  #create new array for anagram
  new = []

  #array of numbers
  numbers = []
  for i in range(0,len(message)):
    numbers.append(i)

  for i in range(0,len(message)): 
    a = random.choice(numbers)
    new.append(original[a])
    numbers.remove(a)

  #converts array to string
  newMessage = ""

  for i in range(0,len(new)):
    newMessage += new[i]

  #redo anagram if message hasn't changed (until it has)
  if (message == newMessage) and (len(message) > 1):
    newMessage = CreateAnagram(message)
  
  return newMessage

#anagram cypher
def Option5():

  #enter message to be encrypted
  print("This is the anagram cypher")
  print("Please enter the message to be encrypted")
  
  message = input()

  #activates CreateAnagram function and stores return value as newMessage
  newMessage = CreateAnagram(message)

  #print result
  print("The anagram is:")
  print(newMessage)

    #user can return to menu or exit program
  print("Return to menu? Y/N")
  Return = input()
  if Return == 'Y':
      return menu()
  elif Return == 'N':
      quit()


#menu is defined
def menu():
    print("Welcome to our encryption/decryption program. Please choose an option (1, 2, 3, 4 or 5):")
    print("Option 1 - monoalphabetic encryption")
    print("Option 2 - polyalphabetic encryption (new key for each letter)")
    print("Option 3 - polyalphabetic encryption (double cipher)")
    print("Option 4 - monoalphabetic decryption")
    print("Option 5 - anagram cipher")
    #user chooses an option
    Option = input()
    if Option == '1':
        Option1()
    elif Option == '2':
        Option2()
    elif Option == '3':
        Option3()
    elif Option == '4':
        Option4()
    elif Option == '5':
        Option5()
    else:
        menu()

#opens menu
menu()
