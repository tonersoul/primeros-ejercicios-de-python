nombre = input("como te llamas?: ")
edad = float(input("que edad tines?: "))
if edad < 18:
    print(nombre.upper() + " eres menor de edad")
else:
    print(nombre.upper() + " eres mayor de edad")