# Variables declaration
userid="arcadebuddy"
password= "906835"

#Username loop
while True:
    
    USERNAME= input("Enter your username:")

    if USERNAME==userid:
        userid=USERNAME #replacing current username
        print("Username is corect!")
        break
    else:
        print("Please enter your correct username!\n")

# Password loop
while True:

    PASSWORD= input("Enter your password:")

    if (PASSWORD==password):
        print("Login successfull!") 
        password=PASSWORD #replacing current password
        print("CURRENT PASSWORD:",password)
        print("CURRENT USERNAME:",userid)
        break
    else:
        print("Please Enter you correct password!\n")

# Usermenu after login
while True:
    print("What do you want to choose from the list:")
    print("1. Change the username")
    print("2. Change the password")
    print("3. Exit, I don't want to change anything!")

    user_choice=input("Enter your choice:") #Taking user's input for further tasks

    if user_choice=="1":
        new_username= input("Enter a new username(e.g Abir Dey): ")

        if new_username==userid:
            print("Userid is same as previous, Please try something new")
        else:
            print("Userid changed successfully!")
            userid=new_username #Replacing old username with the new one
            print("The new username is:",userid)

    elif user_choice=="2":
        new_password= input("Enter a new password (e.g #opbro23): ")

        if (new_password==password):
            print("Password is same as previous, Please try something new")
        else:
            print("Password changed successfully")
            password=new_password #Replacing old password with the new one
            print("The new password is: ",password)

    elif user_choice=="3":
        print("Username and Password doesnot changed")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
