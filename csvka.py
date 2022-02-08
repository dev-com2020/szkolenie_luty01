import csv

# with open('data.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

# with open('data.csv') as file:
#     data = csv.DictReader(file)
#     nowe_dane = [r for r in data]
#     print(nowe_dane[0:3])
#     print(nowe_dane[0].keys())
#     print(nowe_dane[0]['polskie'])

# with open('data.csv', newline='') as file:
#     dialect = csv.Sniffer().sniff(file.read())
#     file.seek(0)
#     reader = csv.reader(file,dialect)
#     print(reader)