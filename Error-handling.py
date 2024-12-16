def file_read_write():
    try:
        # Ask the user for the input and output filenames
        input_file = input("Enter the name of the file to read: ")
        output_file = input("Enter the name of the file to write the modified content: ")
        
        # Open the input file and read its content
        with open(input_file, "r") as infile:
            content = infile.read()
            print("\nOriginal Content:")
            print(content)

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        print(f"\nModified content successfully written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_file}'.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Run the program
file_read_write()
