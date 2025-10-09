import csv

try:
    file_name = input("Enter CSV file name (with .csv): ") # ask user for CSV file
    with open(file_name, 'r') as file:  # open file in read mode
        reader = csv.reader(file)

        row_num = 0
        found_cells = []    # store positions where 'ai' is found
        for row in reader:
            row_num += 1
            for col_num, cell in enumerate(row, start=1):
                
                if 'ai' in cell.lower():    # check if 'ai' is present
                    found_cells.append((row_num, col_num))

        if found_cells:
            print("Cells containing 'ai' (row, column):")
            for r, c in found_cells:
                print(f"({r}, {c})")
        else:
            print("No cells contain 'ai'.")  #no match found

except FileNotFoundError:
    print("Error: File not found.")   # handle missing file

except Exception as e:
    print("Error:", e)  
