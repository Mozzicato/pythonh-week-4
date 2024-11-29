def read_and_modify_file():
    input_filename = input("Enter the filename to read: ")
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"Modified content has been written to '{output_filename}'")
    except IOError:
        print(f"Error: The file '{output_filename}' cannot be written.")

if __name__ == "__main__":
    read_and_modify_file()