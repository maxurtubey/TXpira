import datetime
def fecha_form(list_):
    for row in list_:
        yy = '20' + (row[3][-2:])
        mm = (row[3][2:4])
        dd = (row[3][:2])
        if mm[0] == '0':
            mm = mm[1:]        
        if dd[0] == '0':
            dd = dd[1:]
        yyyy = str(yy)
        año = int(yyyy)
        mes = int(mm)
        dia = int(dd)
        ffvv = datetime.date(año, mes, dia)
        hoy = datetime.date.today()
        exp = (ffvv - hoy)
        row.append(exp.days)
    pass