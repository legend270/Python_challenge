def count_lines_and_words(Customer_Call_List.csv):
    try:
        with open(Customer_Call_List.csv, 'r') as file:
            line_count = 0
            word_count = 0
            
            for line in file:
                line_count += 1
                words = line.split()  # Split by whitespace
                word_count += len(words)
            
            print(f"File: {Customer_Call_List.csv}")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{Customer_Call_List.csv}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{Customer_Call_List.csv}'.")

# Example usage
count_lines_and_words('sample.txt')