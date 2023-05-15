import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "8KUc7ofXpmqiwRAVDQwcayJmQzk7LSWa"
locale = "es_MX"
unit = "k"

while True:
    print("=============================================")
    print("Bienvenido a la navegación a traves de Mapquest")
    print("Para salir del programa, escriba q o quit")
    print("=============================================")
    orig = input("Indique la dirección de Origen: ")
    if orig == "quit" or orig == "q":
        print("Saliendo del Programa")
        break
    dest = input("Indique la dirección de Destino: ")
    if dest == "quit" or dest == "q":
        print("Saliendo del Programa")
        break
    url = main_api + urllib.parse.urlencode({"key":key, "locale":locale, "unit":unit, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = Se ha encontrado una ruta.\n")
        print("=============================================")
        print("Instrucciones desde " + (orig) + " hacia " + (dest))
        print("Duracion del Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Total en Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) )
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; No se ha ingresado un Origen o Destino Valido.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Falta Ingresar Origen o Destino.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")