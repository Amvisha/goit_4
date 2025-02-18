"""
byte_str = 'some text'.encode()
print(byte_str)

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел

for num in [127, 255, 156]:
  print(hex(num))

s = "Привіт!"
utf8 = s.encode()
print(f"UTF-8: {utf8}")
utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")
cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")
s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

# Відкриття текстового файлу з явними вказівками UTF-8 кодування
with open('example.txt', 'w+', encoding='utf-8') as file:
    content = file.read()
    print(content)

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)
"""
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'
