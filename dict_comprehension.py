#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
file_data_frame = pandas.DataFrame(file)
file_dict = {row.letter:row.code for (index, row) in file_data_frame.iterrows()}
print(file_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("What word would you like to spell?").upper()
output = [file_dict[letter] for letter in user_word]
print(output)
