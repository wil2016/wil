def nmeses():
    global meses
    while(1):
        try:
            print("ingrese su cantidad de meses")
            meses=input()
            meses=int(meses)
            while(prestamo<0):
                print("ingrese correctamente su cantidad de meses")
                meses=input()
                meses=int(meses)
            break
        except ValueError:
            print("ingrese correctamente")
    iprestamo()
def iprestamo():
    prestamot=prestamo+(prestamo*cambio/100*meses)
    mest=prestamot/meses
    print("prestamo total",prestamot,"S/")
    print("prestmensual",mest,"S/")
    time.sleep(4)
