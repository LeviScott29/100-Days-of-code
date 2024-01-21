import pandas
#reads csv of letters and phonetics and puts them in dictionary
df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO = {row.letter: row.code for (index, row) in df.iterrows()}

#takes user input and compares it to dictionary to find associated phonetic for each letter
word = input("put in a word").upper()
NATO_return = [NATO[letter] for letter in word]
print(NATO_return)
