# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

# Dictionary of words
words = {
    'madad': 'help',
    'khursi': 'chair',
    'kutta': 'dog'
}

# Ask user for a word
word = input("Enter the word you want meaning of: ")

# Print meaning if found
print("Meaning:", words.get(word, "Word not found"))