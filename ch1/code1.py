def write_memo(file_path, memo):
    with open(file_path, 'a') as file:
        file.write(memo + '\n')

def read_memo(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print("\n--- Memo Content ---")
            print(file_content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = "data/memo.txt"

    while True:
        print("\n1. Write Memo")
        print("2. Read Memo")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            memo = input("Enter your memo: ")
            write_memo(file_path, memo)
            print("Memo added successfully.")
        elif choice == '2':
            read_memo(file_path)
        elif choice == '3':
            print("Exiting the memo application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
