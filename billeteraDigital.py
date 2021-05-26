# LISTA DE LAS MONEDAS DE que soporte monedas registradas en coinmarketcap.com

import requests

headers = {'Accepts': 'application/json',
           'X-CMC_PRO_API_KEY':  '250f64bb-56e4-4a33-8831-6abacfd85df9'}


data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                    headers=headers).json()

lista = {}
for moneda in data['data']:
    a = moneda["symbol"]
    b = moneda["quote"]["USD"]["price"]
    lista[a] = b


# Funcion que valida que la moneda difitada se encuentra en coinmarketcap.com


def validarMoneda(listaCoin):
    nombreMoneda = input("Nombre de la moneda: ").upper()

    while nombreMoneda not in listaCoin:
        print(nombreMoneda, "no se encuentra en coinmarket")
        nombreMoneda = input("ingrese el nombre de la cryptomoneda")

    else:

        return nombreMoneda


# Funcion para verificar que el usuario da numeros para seleccionar la tarea

def numeroReal(comentario):
    while True:
        try:
            numero = float(input(comentario))
            break
        except ValueError:
            print("debe ingresar un numero")
    return numero


def verificarTareas(numeroTareas):
    accion = numeroReal(
        "Ingresa el numero que corresponde a la tarea que requiere realizar: ")
    while not (0 < accion <= numeroTareas):

        print("Esta accion no se encuentra disponible")
        accion = numeroReal(
            "Ingresa el numero que corresponde a la tarea que requiere realizar: ")
    return accion

###FUNCION MENÚ Y TAREAS##


def menu(task, listaCoin, listNom, listCan, lisCotiz, codigoEnvio):
    if task == 1:
        monedaCoin = validarMoneda(listaCoin)
        cantidadRecibir = float(input("Cantidad a recibir: "))
        codigo = input("Codigo quien envía: ")
        if monedaCoin in listNom:
            i = listNom.index(monedaCoin)
            listCan[i] += cantidadRecibir
        else:
            listNom.append(moneda)
            listCan.append(cantidadRecibir)
        print("Operacion exitosa, a recibido", cantidadRecibir, monedaCoin)

        print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
        task = verificarTareas(6)
        menu(task, listaCoin)
    elif task == 2:
        print("menu2")
        print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
        task = verificarTareas(6)
    elif task == 3:
        print("menu3")
        print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
        task = verificarTareas(6)
    elif task == 4:
        print("menu4")
        print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
        task = verificarTareas(6)
    elif task == 5:
        print("menu5")
        print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
        task = verificarTareas(6)
    else:
        print("Gracias, te esperamos pronto.")


# menú principal
print("¿Que deseas realizar??\n1.Recibir cantidad\n2.Trasnferir monto\n3.Mostrar balance una moneda\n4.Mostrar balance general.\n5.Mostrar hístorico de transacciones.\n6.Salir del programa.")
crypto, cant, cotiz, codigoEnviador = [], [], [], []

tarea = verificarTareas(6)
menu = menu(tarea, lista, crypto, cant, cotiz, codigoEnviador)
