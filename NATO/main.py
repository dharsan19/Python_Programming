import pandas

user_input = "Dharsan"

df = pandas.read_csv("NATO/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    try:
        phonetic_code = [phonetic_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabet please. ")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()