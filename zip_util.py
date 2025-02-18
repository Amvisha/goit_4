# import shutil
# print(shutil.disk_usage('c:/'))


from pathlib import Path
"""
p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix:", p.suffix)
print("Parent:", p.parent)

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text())
print("Exists:", p.exists())

# Початковий шлях
base_path = Path("/usr/bin")
# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

current_working_directory = Path("C:/Users/Studio/PycharmProjects/goit_4")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)

# Початковий шлях до файлу
original_path = Path("documents/example.txt")
# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)

# Початковий шлях до файлу
original_path = Path("documents/example.txt")
# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)

original_path = Path("example.txt")
# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)

# Створення об'єкту Path для файлу
file_path = Path("example.txt")
# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")
# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")
# Бінарні дані для запису
data = b"Python is great!"
# Запис байтів у файл
file_path.write_bytes(data)
# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)

# Створення об'єкту Path для директорії
directory = Path("./.idea")
# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)

directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)
directory = Path('/my_directory/new_folder')
directory.rmdir()
"""
path = Path("./.idea")
# Перевірка існування
if path.exists():
    print(f"{path} існує")
# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")
# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

import shutil

# Вихідний і цільовий файли
source = Path('test.txt')
destination = Path('file.txt')
# Копіювання файла
shutil.copy(source, destination)

# Вихідний і цільовий шляхи
source = Path('file.txt')
destination = Path('file1.txt')
# Переміщення файла
shutil.move(source, destination)

import time

file_path = Path("file1.txt")
# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")
# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')
# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')
file_path.unlink(missing_ok=True)
