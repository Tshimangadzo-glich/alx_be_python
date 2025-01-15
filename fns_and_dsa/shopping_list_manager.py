def display_menu():
    print(f"\nShopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit") 

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            remove_item = input("Enter the item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print(f"'{remove_item}' not found in your shopping list." )

        elif choice == '3':
            if shopping_list:
                print("Your shopping list:")
                for i in shopping_list:
                    print(f"{i}. ")
            else:
                print("Your shopping list is currently empty.")
        elif choice == '4':
            print ("Goodbye!")
            break
        else:
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
