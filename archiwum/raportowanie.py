from datetime import datetime

TEMPLATE = '''
Raport z dnia pracy
-----------------
Data: {date}
Liczba klientów: {num_client}
Łączny czas pracy: {total}
------------------
'''

data = {
    'date': datetime.utcnow(),
    'num_client': 5,
    'total': 376,
}

raport = TEMPLATE.format(**data)
FILENAME = "{date}_raport.txt"
file = FILENAME.format(date=data['date'].strftime('%Y-%m-%d'))
with open(file, 'w', encoding="utf-8") as f:
    f.write(raport)
