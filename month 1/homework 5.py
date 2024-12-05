Geeks ={
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

Geeks.pop('bag')
Geeks['address'] = 'Ibraimova 103/1'
Geeks.update({'phone': '996507052018', 'instagram': '@geeks.edu'})
Geeks['courses'] = set(Geeks['courses'] + ['КММ', ' 1C'])
Geeks['date_of_foundation'] = '2018'
print(f'количество доступных курсов: {len(Geeks['courses'])}')

for key, value in Geeks.items():
    print(f'{key}: {value}')