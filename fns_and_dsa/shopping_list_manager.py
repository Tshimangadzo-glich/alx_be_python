def display_menu():
    print("\nShopping List Manager")
    print("Add Item")
    print("Remove Item")
    print("View List")
    print("Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice ")

        if choice == '1':
        elif choice == '2':
        elif choice == '3':
        elif choice == '4':
            print ("Goodbye!")
            break
        else:
            print ("Invalid choice. Please try again.")

    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' was not found in the shopping list.")

if __name__ == "__main__":
    main()
