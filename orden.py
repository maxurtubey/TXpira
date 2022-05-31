import datetime
from operator import itemgetter
from tabulate import tabulate

def sort(list_):
    hoy = datetime.date.today()
    print()
    print(f'La fecha actual es: {hoy}')
    ordn = sorted(list_, key=itemgetter(5))
    return ordn