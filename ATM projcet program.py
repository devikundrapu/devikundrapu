 # write  a ATM  program in 
#create an atm program using functions
  
card_number="1234-5678-9012-3456"
pin ="1234"
balance=1000

print("welcom to the ATM!")

while True:
    print("\nATM Menu:")
    print("1.Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4.Change PIN")
    print("5.Exit")

    choice=input("enter your choice:")
    if choice=="1":
      card_number=input("enter  card number:")
      pin_num=input("enter pin:")
    if card_number==card_number and pin_num==pin:
        print(f"current balance:${balance:.2f}")
    else:
          print("Authentication failed.")
    if choice=="2":
     card_number=input("enter card number:")
pin_num=input("enter pin:")
if card_number==card_number and pin_num==pin:
     amount=float(input("enter withdrawal  amount : $"))
     if amount > balance:
          print ("insufficient balance.")
     else:
          balance_=amount
          print(f"withdrawal successful. new balance: $ {balance:.2f}")
else:
        print("authentication failed.")
if  choice=="3":
 card_number=input("enter card numbere:")
pin_num=input("enter pin:")
if card_num==card_number and pin_num==pin:
     amount=float(input("enter deposit amount:$"))
     balance+=amount
     print(f"deposit successful. new balanced: $ {balance :.2f}")
else:
     print("authentication failed.")
if choice=="4":
     card_num=input("enter card number:")
pin_num=input("enter pin:")
if card_num==card_number and pin_num==pin:
     new_pin=input("enter new pin:")
     pin=new_pin
     print("pin changed successfully,")
else:
     print("authentication failed.")
if choice == "5":
       print(" exiting atm program .goodbye!")
       Break             
else:
 print ("invalid choice. please try again")


       

