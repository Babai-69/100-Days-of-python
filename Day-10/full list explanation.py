# Create a program that takes input from the user using a menu that helps the user to:
"""
1. Check the list
2. Add an element in the list
3. Remove an element from the list
4. Count how many times a number appears
5. Reverse the list
6. Sort the list
7. Add another list
8. Count the current number of objects in the list
9. Exit
"""

num = [54, 38, 18, 51, 60, 3, 91, 8, 92, 50, 65, 87, 96, 39, 78,
       94, 45, 17, 23, 35, 76, 32, 15, 77, 44, 88, 47, 11, 59,
       74, 100, 14, 22, 85, 49, 37, 5, 1, 53, 9, 75, 93, 20,
       29, 52, 28, 86, 30, 61, 46]

while True:

    print("\nWhat do you want to do with the list?")
    print("1. Check the list numbers")
    print("2. Add a new element in the list")
    print("3. Delete an existing item from the list")
    print("4. Count how many times a number appears")
    print("5. Reverse the list")
    print("6. Sort the list")
    print("7. Add another list")
    print("8. Count the current number of elements")
    print("9. Exit")

    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        print(num)

    elif user_input == 2:

        print("Where do you want to add the element?")
        print("1. At the end of the list")
        print("2. At a specific position in the list")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            input_num = int(input("Enter the number: "))
            num.append(input_num)
            print(num)

        elif user_choice == 2:
            input_num = int(input("Enter the number: "))
            index_num1 = int(input("Enter the index number: "))

            if 0 <= index_num1 <= len(num):
                num.insert(index_num1, input_num)
                print(num)

            else:
                print("Invalid index number!")

        else:
            print("Invalid choice!")

    elif user_input == 3:

        print("From where do you want to remove the element?")
        print("1. From the end of the list")
        print("2. From a specific position")
        print("3. Remove a specific number")

        user_choice2 = int(input("Enter your choice: "))

        if user_choice2 == 1:

            if len(num) > 0:
                removed_num = num.pop()
                print("Removed element:", removed_num)
                print(num)

            else:
                print("The list is empty!")

        elif user_choice2 == 2:

            index_num2 = int(input("Enter the index position: "))

            if 0 <= index_num2 < len(num):
                removed_num = num.pop(index_num2)
                print("Removed element:", removed_num)
                print(num)

            else:
                print("Invalid index position!")

        elif user_choice2 == 3:

            delete_num = int(input("Enter the number: "))

            if delete_num in num:
                num.remove(delete_num)
                print(num)

            else:
                print("Number not found in the list!")

        else:
            print("Invalid choice!")

    elif user_input == 4:

        input_value1 = int(input("Enter the number you want to check: "))

        count = num.count(input_value1)

        print("The number appears", count, "time(s) in the list.")

    elif user_input == 5:

        num.reverse()
        print("Reversed list:", num)

    elif user_input == 6:

        num.sort()
        print("Sorted list:", num)

    elif user_input == 7:

        new_list = []

        num2 = int(input("How many numbers do you want to add? "))

        for i in range(num2):
            input_num = int(input("Enter a number: "))
            new_list.append(input_num)

        num.extend(new_list)

        print("Updated list:", num)

    elif user_input == 8:

        print("Total number of elements:", len(num))

    elif user_input == 9:

        print("Thanks for coming!")
        break

    else:
        print("Please enter the correct value!")

# End of the program