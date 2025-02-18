"""
string1 = "Hello World"
string2 = "hello world"
if string1.casefold() == string2.casefold():
    print("Рядки однакові")
else:
    print("Рядки різні")
"""

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі
# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()
# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()
print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")

