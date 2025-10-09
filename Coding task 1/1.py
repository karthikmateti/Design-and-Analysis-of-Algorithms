try:
    file_name = input("Enter the text file name (with extension): ")  # get file name from user
    with open(file_name, 'r') as file:  # open file in read 
        print(file.read())  # display file content
except FileNotFoundError:
    print("Error: file was not found.")  # if file not found
finally:
    print("\nProgram execution completed.") 
