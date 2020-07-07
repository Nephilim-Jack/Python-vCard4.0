import os
import PyVCard4

with open('Nomes.txt', 'r') as names:
    names = [line.replace('\n', '') for line in names.readlines()]

with open('Números.txt', 'r') as numbers:
    numbers = [line.replace('\n', '') for line in numbers.readlines()]

vc = PyVCard4.VCard(os.getcwd())
vc.company = '{company_here}'

vc.name_num = tuple(((name, num) for name, num in zip(names, numbers)))

vc.create_vcard()
