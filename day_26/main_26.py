import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)
# for (key, value) in df.items():
#     print(value)
# for (index, row) in df.iterrows():
#     print(row)


nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
name = input("Name: ")
print([nato_dict[letter.upper()] if letter.upper() in nato_dict.keys() else letter for letter in name])

