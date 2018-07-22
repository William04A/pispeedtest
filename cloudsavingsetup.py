#coding=UTF-8
import os
import requests
import time
import re

validlanguages = ["sv-se", "en-us"]
class PiSpeedtestExceptions(Exception):

    pass
class SetupExceptions(PiSpeedtestExceptions):
    pass

class QuitRequestedByUser(SetupExceptions):
    pass

class NoValidLanguageDefined(SetupExceptions):
    pass

def setup():
    verify = "YES"
    print("Contacting registration server, please wait.")
    if verify == "YES":
        apikeyrequest = requests.get("https://pispeedtestcloudsaving.pythonanywhere.com/create_api_key")

        if "Success!" in apikeyrequest.text:
            status = "Success."

            apikey = apikeyrequest.text.replace("Success! Your application key is ", "").replace(
                "Keep it secret. The key allows access to all of your documents and speedtest results.",
                "").replace(".", "")
        else:

            status = "Error."
        print("Response from server: " + apikeyrequest.text + " Detected status: " + status)
        if status == "Success.":
            print("Writing API-key to text document for offline usage...")

            with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "w+") as apikeytextfile:
                apikeytextfile.write(
                    "Please do not modify this file! It contains an API-key for cloud-saving speedtests made with the application PiSpeedtest." + "\n")

                apikeytextfile.write(apikey + "\n")
            with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), ) as cloudsavingstatusfile:

                cloudsavingstatusfile.truncate()
                cloudsavingstatusfile.write("ENABLED" + "\n")
            print("The API-key was saved. The cloud saving setup for PiSpeedtest is now complete.")
            print("✔ Cloud saving will be enabled the next time that you start PiSpeedtest.")
        else:
            print(
                "It seems like you have chosen not to set up cloud saving for PiSpeedtest. The application will quit in ten seconds.")
            time.sleep(10)
            raise QuitRequestedByUser("The user asked to quit the setup.")


with open(os.path.join(os.getcwd() + "\\configurationfiles\\" + "languageconfiguration.txt"), "r+") as languageconfigurationsfile:

    languageconfigurationsfilecontent = languageconfigurationsfile.read().splitlines()
    languageconfiguration = languageconfigurationsfilecontent[1]
if languageconfiguration in validlanguages:
    if languageconfiguration == "sv-se":
        intromessage = "Detta program kommer att hjälpa dig att konfiguera PiSpeedtest´s \"moln-lagring\"."
        intromessage2 = "Denna funktion är helt gratis och obegränsad och tar cirka 10 sekunder att ställa in så länge du inte vill läsa en kort guide."
        invalidmodeselected = "PiSpeedtest kunde inte hitta ett giltigt läge. Vänligen starta om programmet och se till att du skriver in dina val korrekt."
        optiontext = "Skriv \"TUTORIAL\" för en kort genomgång (cirka 120 ord) eller \"SETUP\" för att ställa in molnlagring. "
        foundapikeyfile = "Filen \"apikey.txt\" hittades. Letar efter API-nyckel."
        apikeyalreadyexists = "Det verkar som att du redan har en API-nyckel för PiSpeedtest molnlagring."

        verifyinput = "Vill du fortfarande fortsätta? Om du gör det så kommer din nuvarade API-nyckel att sluta användas på enheten. YES eller NO: "
        closingprogram = "Okej. Programmet stängs om tio sekunder."
        creatingnewapikey = "Okej. En ny API-nyckel kommer att skapas."
        couldnotunderstandoption = "Setup-programmet kunde inte förstå ditt val. Det kommer att avslutas om tio sekunder. Vänligen starta om det och välj ett gilltigt val."
        invalidapikey = "Det verkar som att du redan har en API-nyckel för PiSpeedtest, men att den är felaktig."
        verifymessage = "Vill du fortfarande fortsätta och skapa en ny API-nyckel? Skriv YES eller NO och tryck sedan på enter: "
        cloudsavingnotsetup = "Det verkar som att du inte ställt in PiSpeedtest´s molnlagring än eller att du vill uppdatera tjänsten."
        tutorialmessage = "Guiden visas mening-för-mening. För att visa nästa mening, tryck på enter-knappen."


        contactingserver = "Kontakar registrings-server, vänligen vänta..."
        detectedstatusmessage = " Detekterad status: "
        serverresponsemessage = "Svar från server: "
        savingtotextfile = "Sparar API-nyckel till textdokument för användning offline..."
        apikeysaved = "API-nyckeln har sparats. Molnlagrings-setupprogrammet för PiSpeedtest är nu klart."
    elif languageconfiguration == "en-us":

        intromessage = "This program will help you get started with PiSpeedtest´s cloud saving feature."
        intromessage2 = "This feature is totally free and unlimited and takes about 10 seconds to set up unless you want to read a short tutorial."
        invalidmodeselected = "PiSpeedtest could not detect a valid mode. Please restart the program and make sure to type your option correctly."
        optiontext = "Type \"TUTORIAL\" for a short tutorial (about 120 words) or \"SETUP\" to set up cloud saving. "
        foundapikeyfile = "The file \"apikey.txt\" was found. Looking for API-key."
        apikeyalreadyexists = "It seems like you already have a valid API-key for PiSpeedtest cloud saving."
        verifyinput = "Do you still want to continue? Doing so will stop usage of the current API-key on this device. YES or NO: "
        closingprogram = "Okay. Closing the setup program in ten seconds."
        creatingnewapikey = "Okay, creating a new api key."
        couldnotunderstandoption = "The setup program could not understand your option. It will quit in ten seconds. Please run it again and select a valid option."

        invalidapikey = "It seems like you already have a cloudsaving API, but that it is invalid."
        verifymessage = "Do you still want to continue and create a new API-key? Type YES or NO and then press enter: "
        cloudsavingnotsetup = "It seems like you want to update PiSpeedtest´s cloudsaving or that you haven´t enabled it yet."
        tutorialmessage = "The tutorial will display sentence-by-sentece. Press the enter key to show the next sentence."
        contactingserver = "Contacting registration server, please wait..."
        serverresponsemessage = "Response from server: "
        detectedstatusmessage = " Detected status: "
        savingtotextfile = "Writing API-key to text document for offline usage..."
        apikeysaved = "The API-key was saved. The cloud saving setup for PiSpeedtest is now complete."
else:
    print("The current language configuration is invalid. Please edit the file \"languageconfiguration.txt\" and then run this program again.")
    raise NoValidLanguageDefined("No valid language has been defined. Please edit the file \"languageconfiguration.txt\" and then run this program again.")
print(intromessage)
print(intromessage2)

option = input(optiontext)

if option == "SETUP":

    try:
        with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"), "r") as apikeytextfile:
            print(foundapikeyfile)

            filecontents = apikeytextfile.read().splitlines()


        if len(filecontents[1].replace(" ", "")) == 25 and len(re.findall(r"[A-Z]", filecontents[1].replace(" ", ""))) + len(re.findall(r"[a-z]", filecontents[1].replace(" ", ""))) == 20 and len(re.findall(r"[1-9]", filecontents[1].replace(" ", ""))) == 5:

            print(apikeyalreadyexists)

            verify = input(verifyinput)

            if verify == "YES":

                print(creatingnewapikey + "\n")
            elif verify == "NO":
                print(closingprogram)

                time.sleep(10)
                exit()
            else:
                print(couldnotunderstandoption)
                time.sleep(10)
                raise QuitRequestedByUser("The user asked to quit the setup.")
        else:
            print(invalidapikey)
            verify = input(verifymessage)

            if verify == "YES":
                print(contactingserver)
                if verify == "YES":
                    apikeyrequest = requests.get("https://pispeedtestcloudsaving.pythonanywhere.com/create_api_key")

                    if "Success!" in apikeyrequest.text:
                        status = "Success."

                        apikey = apikeyrequest.text.replace("Success! Your application key is ", "").replace("Keep it secret. The key allows access to all of your documents and speedtest results.","").replace(".", "")
                    else:

                        status = "Error."
                    print(serverresponsemessage + apikeyrequest.text + detectedstatusmessage + status)
                    if status == "Success.":
                        print(savingtotextfile)

                        with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\apikey.txt"),"w+") as apikeytextfile:
                            apikeytextfile.write("Please do not modify this file! It contains an API-key for cloud-saving speedtests made with the application PiSpeedtest. (Swedish: Modifiera inte denna fil, tack! Den innehåller din API-nyckel för att ladda upp resultat i molnet med PiSpeedtest):" + "\n")

                            apikeytextfile.write(apikey + "\n")
                        with open(os.path.join(os.getcwd() + "\\cloudsaving\\savedata\\status.txt"), "w") as cloudsavingstatusfile:

                            cloudsavingstatusfile.truncate()
                            cloudsavingstatusfile.write("ENABLED" + "\n")
                        print(apikeysaved)
                        print("✔ Cloud saving will be enabled the next time that you start PiSpeedtest.")
                    else:
                        print("It seems like you have chosen not to set up cloud saving for PiSpeedtest. The application will quit in ten seconds.")
                        time.sleep(10)
                        raise QuitRequestedByUser("The user asked to quit the setup.")

                print(creatingnewapikey + "\n")
            elif verify == "NO":
                print(closingprogram)

                time.sleep(10)
                raise QuitRequestedByUser("The user asked to quit the setup.")

            else:
                print(couldnotunderstandoption)
                time.sleep(10)
                raise QuitRequestedByUser("The user asked to quit the setup.")
    except QuitRequestedByUser:
        exit()
    except NoValidLanguageDefined:

        exit()

    print(cloudsavingnotsetup)

elif option == "TUTORIAL":

    swedishtutorial = ['Att spara data i molnet är någonting du gör ganska ofta,', 'Oavsett om det är din smartphone´s backup eller dina email, finns molnet där för att hjälpa dig.', 'PiSpeedtest tillåter dig att spara speedtest-data i molnet.', 'Denna tjänst är helt kostnadsfri och obegränsad.', 'Du har två val i nuläget: att se speedtest-data online eller ladda ner det.', 'Båda val ger dig samma data som om du skulle öppna en fil i mappen "speedtestresults".', 'Dessa val får du länkar till när alla speedtest har körts.', 'Efter ett kort setup-program så kommer en "API-nyckel" att skapas, och det kommer att vara din åtkomstnyckel för PiSpeedtest´s molnlagring.', 'Setup-programmet kommer nu att startas.']

    englishtutorial = ['Cloud saving your data is something you do quite often.', 'Whether it is your smartphone´s backup or your emails, the cloud is there to help you.', 'PiSpeedtest also allows you to cloud save your speedtest data.', 'This service is totally free and also unlimited.', 'You have two options at the moment: to view the speedtest data online or to download it.', 'Both options gives you the same data as opening a file found in the directory "speedtestresults".', 'You get links to these options when all speedtests have been run.', 'After a setup where the program contacts an external server, an "API-key" will be created, which will be an access key for PiSpeedtest Cloud saving.', 'The setup will now begin.']

    print(tutorialmessage)
    if languageconfiguration == "en-us":
        for i in range(len(englishtutorial)):
            print(englishtutorial[i])
            input()
        setup()
    elif languageconfiguration == "sv-se":
        for i in range(len(swedishtutorial)):
            print(swedishtutorial[i])
            input()
        setup()
else:
    print(invalidmodeselected)
