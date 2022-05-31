import datetime
def newfecha(fvenc):
    yy = '20' + (fvenc[-2:])
    mm = (fvenc[2:4])
    dd = (fvenc[:2])
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
    return exp