import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "tkn3E4zSSF1mXxn8h5KuQEUXFISYyzgp"


while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "Q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "Q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.3f}".format((json_data["route"]["distance"])*1.61)))
#        print("Fuel Used (Lts): " + str("{:.3f}".format(json_data["route"]["fuelUsed"])*3.78))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.3f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")