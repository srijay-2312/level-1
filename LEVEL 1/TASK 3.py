def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_name = input("Enter the filename (with extension): ")
count_words_in_file(file_name)