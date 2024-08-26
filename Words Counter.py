def count_words(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Return the total number of words
            return len(words)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

# Replace 'your_file.txt' with the actual name of your text file
file_name = 'waleed-067-nlp.txt'

word_count = count_words(file_name)

if word_count is not None:
    print(f'Total number of words: {word_count}')


# =====================================================================================================