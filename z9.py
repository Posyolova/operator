shootrange = float(input('введите дальность выстрела - '))
if shootrange >28 and shootrange <30:

    print ('попал прям в цель')

elif shootrange >=30:

    print ('перелетело')

elif shootrange >0 and shootrange <=28:

    print ('недолёт!')

elif shootrange >=0:

    print ('не бей по своим ')
