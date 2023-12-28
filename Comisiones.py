nombre = input("Por favor, dime como te llamas: ")
ventas = int(input("Dime tus ventas totales de este mes: "))

comision = round(ventas * 15 / 100,2)

print(f"Hola {nombre}, tus comisiones por las ventas de este mes son de ${comision} pesos")