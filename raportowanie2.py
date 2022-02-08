from datetime import datetime
from jinja2 import Template

with open('template.html',encoding='utf-8') as file:
    template = Template(file.read())

data = {
    'date': datetime.utcnow(),
    'num_client': 5,
    'total': 376,
}

with open('raport2.html','w') as file:
    file.write(template.render(data))