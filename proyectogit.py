#PROYECTO FINAL
#El monto debe de ser positivo
#Se debe de validar que los datos sean correctos y que se capture hasta que se haga de manera correcta
#Los dias son: lunes, martes, miercoles, jueves y viernes
#REPORTES: Cuantos días ahorro? Cuanto es el monto total ahorrado?, cual fue el dia que mas ahorró y cuanto?
#Aplicar funciones

#variables auxiliares (Contadoras, acumuladoras, sumadoras)

dias_ahorrados, ahorro_semana, mayor_ahorro, dia_mayor_ahorro = 0, 0, 0, None 
print("-------MI BANCO PERSONAL-------")
while True:
    while True:
        dia = input("Digite el día: ").title()
        if dia == "Lunes" or dia == "Martes" or "Miercoles" or dia == "Jueves" or dia == "Viernes":
            break
        else:
            print("Digite un dia entre lunes y viernes")
        continue

    while True:
        try:
            monto = float(input("Digite el valor del ahorro del día: "))
        except:
            print("Debe de digitar un valor numérico")
            continue
        if monto < 0:
            print("Su ahorro del día no puede ser negativo")
            continue
        else:
            break
        
    if mayor_ahorro < monto:
        mayor_ahorro = monto
        dia_mayor_ahorro = dia
    ahorro_semana += monto
    dias_ahorrados += 1 
    
    print("El día {} se ahorró ${:,.2f}".format(dia, monto))
    
    otro = input("Desea continuar con otro dia? (SI-NO): ").upper()
    if otro == "SI":
        continue
    else:
        break
    
print("----REPORTES----")
print("Ahorro durante {} dias de la semana".format(dias_ahorrados))
print("El total ahorrado en la semana fue de: ${:,.2f}".format(ahorro_semana))
print("El {} fue el de mayor ahorro con ${:,.2f}".format(dia_mayor_ahorro, mayor_ahorro))