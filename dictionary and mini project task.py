#  dictionary  mini project 
# dictionary management system
dictionary= {}
while True:
    print("\n dictionary management system")
    print("1. add a word")
    print("2. search  for meaning")
    print("3. display all word")
    print("4.  update meaning")
    print("5. delete word")
    print("6. exit")

    choice =input("enter your choice:")
    if  choice == "1":
        word=input("enter the  word:")
        meaning=input("enter the meaning:")
        dictionary[word]= meaning
        print("word added!")

    elif choice=="2":
       word= input("enter the  word to search:")
       if word in dictionary:
           print(dictionary [word])
       else:
           print("word not found!")

    elif choice=="3":
        if not dictionary:
            print("the dictionary is empty.")
        else:
            print("list of words  and their meaning:")
        for word, meaning in dictionary.items():
            print(f"{word}: {meaning}")

    elif choice=="4":
        word=input("enter the word to update:")
        if word in dictionary:
            new_meaning=input("enter the new meaning:")
            dictionary[word]=new_meaning
            print("meaning updated!")

    elif choice=="5":
        word=input("enter the word to delete:")
        if word in dictionary:
            del dictionary[word]
            print("word deleted!")
        else:
            print("word not found!")

    elif choice=="6":
            print(" exiting  the program.goodbye!")
            break
    else:
        if choice!= "1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6":
    
           print("invalid choice.please try again")
