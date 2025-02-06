# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()



