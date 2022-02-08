import os
import re
from bs4 import UnicodeDammit

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         print(file)

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         full = os.path.join(root, file)
#         print(full)

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.txt'):
#             full = os.path.join(root, file)
#             print(full)


# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if re.search(r'[1]', file):
#             full = os.path.join(root, file)
#             print(full)

with open('nowy.txt', 'rb') as file:
    content = file.read()

sug = UnicodeDammit(content)
print(sug.original_encoding)
print(sug.unicode_markup)

