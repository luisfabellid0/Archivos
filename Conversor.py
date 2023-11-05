# Define una función que muestra el menú de opciones
def menu():
    print("1. Convertir decimal a binario")
    print("2. Convertir binario a decimal")
    print("3. Convertir decimal a hexadecimal")
    print("4. Convertir hexadecimal a decimal")
    print("5. Convertir dirección IP a binario")
    print("6. Salir")

# Función que convierte un número decimal a binario
def decimal_a_binario(decimal):
    return bin(decimal).replace("0b", "")

# Función que convierte un número binario a decimal
def binario_a_decimal(binario):
    return int(binario, 2)

# Función que convierte un número decimal a hexadecimal
def decimal_a_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")

# Función que convierte un número hexadecimal a decimal
def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

# Función que convierte una dirección IP a su representación binaria
def ip_a_binario(direccion_ip):
    octetos = direccion_ip.split(".")
    binario = ""
    for octeto in octetos:
        binario += format(int(octeto), '08b') + "."
    return binario[:-1]

# Bucle principal que muestra el menú y procesa la opción seleccionada
while True:
    menu()
    opcion = input("Selecciona una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        decimal = int(input("Ingresa un número decimal: "))
        print(f"Binario: {decimal_a_binario(decimal)}")
    elif opcion == "2":
        binario = input("Ingresa un número binario: ")
        print(f"Decimal: {binario_a_decimal(binario)}")
    elif opcion == "3":
        decimal = int(input("Ingresa un número decimal: "))
        print(f"Hexadecimal: {decimal_a_hexadecimal(decimal)}")
    elif opcion == "4":
        hexadecimal = input("Ingresa un número hexadecimal: ")
        print(f"Decimal: {hexadecimal_a_decimal(hexadecimal)}")
    elif opcion == "5":
        direccion_ip = input("Ingresa una dirección IP en formato x.x.x.x: ")
        print(f"Binario: {ip_a_binario(direccion_ip)}")
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
