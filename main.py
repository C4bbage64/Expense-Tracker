import csv_operations
import user_interface

def main():
    # Initialize the CSV file
    csv_operations.init_file()

    # Start the main menu loop
    user_interface.main_menu()

if __name__ == "__main__":
    main()
