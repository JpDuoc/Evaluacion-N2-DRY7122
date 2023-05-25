import urllib.parse
import requests

main_api = "https://mapquestapi.com/directions/v2/route?"
key = "6w6V1DjOrOqJofkxwyzFzL1rv5Tdj7Kr"

while True:
   origen = input("Inicio: ")
   if origen == "quit" or origen == "q":
        break
   destino = input("Destino: ")
   if destino == "quit" or destino == "q":
        break
   url = main_api + urllib.parse.urlencode({"key": key, "from":origen, "to":destino})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("-----------------------------------")
        print("----------------------------------------------")
        print("En dirección desde " + (origen) + " hasta " + (destino))
        print("Tiempo de viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.2f}".format ((json_data["route"]["distance"])*1.61)))
        print("----------------------------------------------")
        print("-----------------------------------")
        for each in json_data["route"] ["legs"] [0] ["maneuvers"]:
            print ((each["narrative"]) + " (" + str("{:.2f}".format ((each["distance"])*1.61) + "km)"))
        print("-----------------------------------\n")
