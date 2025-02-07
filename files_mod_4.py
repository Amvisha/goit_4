"""
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)
fh.close()

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)
fh.close()

fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(1)
second = fh.read(1)
print(second)  # 'e'
fh.close()

fh = open("test.txt", "w+")
fh.write("hello!")
position = fh.tell()
print(position)  # 6
fh.seek(1)
position = fh.tell()
print(position)  # 1
fh.read(2)
position = fh.tell()
print(position)  # 3
fh.close()
"""
fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
    fh.close()
