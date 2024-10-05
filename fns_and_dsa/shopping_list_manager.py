shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter add item name: ")
            shopping_list.append(item)
            print(shopping_list)
            
        elif choice == '2':
            item = input("Enter remove item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(shopping_list)
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            print(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




