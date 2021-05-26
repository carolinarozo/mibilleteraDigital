################# PROGRAMA DE UNA BILLETERA DIGITAL###########################
from datetime import datetime  # trabajar con fecha

# LISTA DE LAS MONEDAS DE que soporte monedas registradas en coinmarketcap.com
import requests

headers = {'Accepts': 'application/json',
           'X-CMC_PRO_API_KEY':  '250f64bb-56e4-4a33-8831-6abacfd85df9'}


data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                    headers=headers).json()


# contiene el simbolo y la cotizacion en USD de cada moneda que se encuentra en coinmarket

diccionarioCoin = {}
for moneda in data['data']:
    a = moneda["symbol"]
    b = moneda["quote"]["USD"]["price"]
    diccionarioCoin[a] = b

# contiene el symbolo y el nombre
diccionarioCoinName = {}
for moneda in data['data']:
    a = moneda["symbol"]
    b = moneda["name"]
    diccionarioCoinName[a] = b


# Funcion que valida que la moneda digitada se encuentra en coinmarketcap.com


def validarMoneda(listaCoin):
    nombreMoneda = input(
        "Ingrese la moneda a la que quiere realizar transacción (BTC,ETH, ect..): ").upper()

    while nombreMoneda not in listaCoin:
        print(nombreMoneda, "no se encuentra en coinmarket")
        nombreMoneda = input("Nombre de la moneda: ").upper()

    else:

        return nombreMoneda

# Funcion para verificar que se digito un numero


def numeroReal(comentario):
    while True:
        try:
            numero = float(input(comentario))
            break
        except ValueError:
            print("debe ingresar un numero")

    return numero

# fUNCION QUE VERIFICA SI ES UN NUMERO POSITIVO


def numeroPositivo(comentario):
    while True:
        numero = numeroReal(comentario)
        if numero < 0:
            print("Debe digitar un número positivo")
        else:
            break
    return numero


# LISTA DE Cryptos
crypto = []
for moneda in data['data']:
    a = moneda["symbol"]
    crypto.append(a)

# Se convierte en tupla para que no sea modificada
cryptos = tuple(crypto)
# cantidades que tiene por cada moneda
cant = []
for x in range(len(crypto)):
    cant.append(0)

operacion = []  # contiene la lista de la operacion que se realizó retiro o deposito
monedaOperacion = []  # la moneda en que se hizo la transaccion
fechaOperacion = []  # la fecha que se relaizó la transaccion
codigoUsuario = []  # codigo de usuario
cantidadOperacion = []  # la cantidad que se recibio o se retiró

while True:
    # menu
    print("\n-----Menú-----\n¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.\n")
    menu = input("Ingresa un número válido de opción del menú:")
    if menu == "1":  # recibir cantidad
        monedaCoin = validarMoneda(cryptos)
        cantidadRecibir = numeroPositivo(
            "Digite la cantidad a recibir en "+monedaCoin + ": ")
        codigoR = input("Codigo quien envía: ")
        i = cryptos.index(monedaCoin)
        cant[i] += cantidadRecibir
        operacion.append("Deposito")
        monedaOperacion.append(monedaCoin)
        fechaActual = datetime.now()
        fechaOperacion.append(fechaActual.strftime(
            "%A %d de %B del %Y hora %H:%M:%S"))
        codigoUsuario.append(codigoR)
        cantidadOperacion.append(cantidadRecibir)

        print("Operacion exitosa, has recibido", cantidadRecibir,
              monedaCoin, "del codigo de referencia", codigoR)
    elif menu == "2":  # Transferencias
        monedaCoin = validarMoneda(cryptos)
        cantidadTransferirUSD = numeroPositivo(
            "Digite la cantidad a transferir en USD: ")
        cantidadTransferir = cantidadTransferirUSD/diccionarioCoin[monedaCoin]
        codigoT = input("Codigo destinatario: ")
        i = cryptos.index(monedaCoin)
        if cant[i]-cantidadTransferir < 0:
            print("Fondos insuficientes")
        else:
            cant[i] -= cantidadTransferir
            print("operacion exitosa, transfirió",
                  cantidadTransferir, monedaCoin, "al codigo de referencia ", codigoT)
            operacion.append("Transferencia")
            monedaOperacion.append(monedaCoin)
            fechaActual = datetime.now()
            fechaOperacion.append(fechaActual.strftime(
                "%A %d de %B del %Y hora %H:%M:%S"))
            codigoUsuario.append(codigoT)
            cantidadOperacion.append(cantidadTransferir)
    elif menu == "3":  # BALANCE DE UNA MONEDA DETERMINADA
        monedaCoin = validarMoneda(cryptos)
        i = cryptos.index(monedaCoin)
        print("----Balance de la moneda", diccionarioCoinName[monedaCoin], "\n cantidad: ", cant[i], monedaCoin,
              " Saldo: ", cant[i]*diccionarioCoin[monedaCoin], "USD")
    elif menu == "4":  # BALANCE GENERAL
        print("----BALANCE GENERAL----")
        totalUSD = 0
        for i in range(len(cryptos)):
            print("Moneda: ", diccionarioCoinName[cryptos[i]], " Cantidad: ", cant[i], cryptos[i],
                  " Saldo: ", cant[i]*diccionarioCoin[cryptos[i]], "USD")
            totalUSD += cant[i]*diccionarioCoin[cryptos[i]]

        print("\n                              Monto Total USD: ", totalUSD)

    elif menu == "5":  # hISTORICO DE TRANSACCIONES
        print("\n----Historico de transacciones----")
        for i in range(len(operacion)):
            print("Tipo de operacion: ", operacion[i], ". Fecha: ", fechaOperacion[i], " .Codigo de usuario:  ",
                  codigoUsuario[i], ". Suma de: ", cantidadOperacion[i], monedaOperacion[i], cantidadOperacion[i]*diccionarioCoin[monedaOperacion[i]], "USD")
    elif menu == "6":  # Salir del programa
        print("!Gracias!, te esperamos pronto.")
        break
    else:  # para una opcion invalida
        print("Por favor ingresa una opción válida")
