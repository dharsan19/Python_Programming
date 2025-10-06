import pandas

user_input = "Dharsan"

df = pandas.read_csv("NATO/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

phonetic_code = [phonetic_dict[letter.upper()] for letter in user_input]

print(phonetic_code)