import speedtest

import time


import requests
import os
#Defining errors - those will be implemented in the future (probably in version 2.1 or later).

class PiSpeedtestErrors(Exception):
    pass
class NoModeDefinded(PiSpeedtestErrors):
    pass
class FileError(PiSpeedtestErrors):
    pass
downloadlist = []
uploadlist = []
pinglist = []

smallestkbitsup = 1000
largestkbitsup = 0
smallestkbitsdown = 1000
largestkbitsdown = 0
noconnection = 0
fileversionnumber = "1.8"
allowedmodes = ["BETA MODE", "STABLE", "COMPATIBLE"]
loadconfig = [0, 0, 0, 0, 0]
print("PiSpeedtest " + fileversionnumber + ".")
#Language settings:
approved_languages = ["sv-se", "en-us"] #To add a language that´s not in the list, make sure to add its name here.
languageconfigpath = os.path.join(os.getcwd() + "/configurationfiles/languageconfiguration.txt")
try:
    with open(languageconfigpath, "r+") as languagecofigurationfile:
        languageconfig = languagecofigurationfile.read().splitlines()
except:
    print("Could not find language configuration. Please make sure that \"languageconfiguration.txt\" is in the directory /configurationfiles.")
    languageconfig = ["Configuration not found." + "ConfigurationNotFound"]
if languageconfig[1] not in approved_languages:
    print("The current language configuration is not valid. Please check the file languageonfiguration.txt. Valid languages are:")
    for i in range(len(approved_languages)):
        print(approved_languages[i])
    languageconfiguration = "sv-se"
    print("For this time, the language has been set to sv-se, Swedish.")
else:
    print("Language configuration " + str(languageconfig[1]) + " found.")
    languageconfiguration = languageconfig[1]
print("\n")
#Language configuration - feel free to add your own languages here!
if languageconfiguration == "sv-se":
    pretestresults = "Pre-test-resultat: Ping till https://www.google.com. Resultat: "
    pretestresults2 = " sekunder."
    nointernetconnectionmessage = "En aktiv internetuppkopppling kunde inte hittas."
    lookingforupdatesmessage = "Letar efter uppdateringar..."
    latestversionmessage = "Senaste versionen av PiSpeedtest är: "
    youhavethelatestversionmessage = "Du har den senaste versionen av PiSpeedtest"
    initialspeedtestinformation = "För att få programmet att fungera optimalt så körs ett \"speedtest\" för att mäta tid m.m. Vänligen vänta."
    speedtestran = "Ett speedtest har nu körts. Det tog: "
    speedtestseconds = " sekunder."
    programmodes = "Programlägen:"
    stablemode = "STABLE - Kör de stabila funktionerna i PiSpeedtest."
    betamode = "BETA MODE - Betafunktioner som kan innehålla buggar."
    compatiblemode = "COMPATIBLE - Välj detta läge för kompatibilitet med Mac, vissa Linuxsystem eller andra system än Windows. En stabil version kommer att köras, inte en betaversion."
    pleaseselectaspeedtestmodemessage = "Vänligen välj ett PiSpeedtest-läge genom att skriva dess namn och trycka på enter: "
    programdurationseconds = "Hur länge vill du köra programmet (i sekunder)? 12 timmar = 43 200 sekunder: "

    programdurationminutes = "Hur länge vill du köra programmet (i minuter)? 12 timmar = 720 minuter: "
    howofteninput = "Hur ofta vill du köra programmet (i sekunder) tar cirka "
    seconds = " sekunder. "
    speedtestfilenameinput = "Vilket namn vill du ha på speedtestfilen? Använd inte punkter eller .txt, det läggs till automatiskt. "
    errormessage = "Ett fel inträffade när ett speedtest skulle köras."
    startingspeedtestmessage = "Startar test."
    speedtestcompletedmessage = "Test utfört."
    programdurationmodemessage = "Vill du ange hur länge du vill köra programmet i sekunder eller minuter? (Skriv \"SECONDS\" eller \"MINUTES\" för att välja.)"
    programdurationmodeerror = "Ett fel inträffade. Skrev du rätt när du valde läge? Läget \"MINUTES\" kommer att väljas automatiskt."
    newversionmessage = "Version: "
    newversionmessage2 = " av PiSpeedtest finns tillgänglig. Du har version: "
    newversionmessage3 = " installerad."
    lookingforupdateserror = "Ett fel inträffade när PiSpeedtest sökte efter nya uppdateringar."

    skipdetected = "SKIP DETEKTERAT"
    speedtestconfignotfound = "Kunde inte hitta konfigurationsfilen."
    loadingconfigurationmessage = "Laddar konfiguration..."
    configurationfilealert = "VARNING: KONFIGURATIONSFILER ÄR I BETA. LÄGES-VAL ÄR INTE INTEGRERAT I PiSpeedtest ÄN!"
    configuredmodemessage = "Det konfiguerade läget är: "
    minutes = " minuter."
    configuredspeedtestdurationmessage = "Konfiguerad speedtest-tid: "
    invalidmode = "Konfigurationsfilen innehåller ett felaktigt läge."
    invalidduration = "Konfigurationsfilen innehåller en ogiltig spedtest-tid."
    configuredruneverysecondmessage = "Konfiguerad \"kör var ___ sekund\": "
    runeverysecondinvalid = "\"Kör var ___ sekund\"-konfigurationen är felaktig."
elif languageconfiguration == "en-us":
    pretestresults = "Pre-test-result: Ping to https://www.google.com. Result: "
    pretestresults2 = " seconds."
    nointernetconnectionmessage = "An active internet connection could not be established."
    lookingforupdatesmessage = "Looking for updates..."
    latestversionmessage = "The latest version of PiSpeedtest is: "
    youhavethelatestversionmessage = "You have the latest version of PiSpeedtest."
    initialspeedtestinformation = "To make the program work better, a \"speedtest\" is being run to measure time and more. Please wait."
    speedtestran = "A speedtest has now been run. It took: "
    speedtestseconds = " seconds."
    programmodes = "Program-modes:"
    stablemode = "STABLE - Run the stable and tested functions in PiSpeedtest."
    betamode = "BETA MODE - Functions in beta that might not work properly."
    compatiblemode = "COMPATIBLE - Select this mode for compatibility with more operating systems than Windows, including Mac, some Linux OSes and other operating systems. A stable release is being run, not a beta release."
    pleaseselectaspeedtestmodemessage = "Please select a PiSpeedtest-mode by typing its name and then pressing enter on your keyboard: "
    programdurationseconds = "For how long do you want to run the program (in seconds)? 12 hours = 43 200 seconds: "

    programdurationminutes = "For how long do you want to run the program (in minutes)? 12 hours = 720 minutes: "
    howofteninput = "How often do you want to run the program (in seconds)? A speedtest takes about "
    seconds = " seconds. "
    speedtestfilenameinput = "What name would you like the speedtestfile to have? Do not use any dots or .txt, it will be added automatically. "
    errormessage = "An error occured during the speedtest."
    startingspeedtestmessage = "Starting speedtest."
    speedtestcompletedmessage = "A speedtest has been run."
    programdurationmodemessage = "Do you want to enter how long you want to run the program in seconds or minutes? (Write \"SECONDS\" or \"MINUTES\" to select.) "
    programdurationmodeerror = "An error occured. Did you type everything in correctly when you choosed an option? The option \"MINUTES\" will be selected automatically. "
    newversionmessage = "Version: "
    newversionmessage2 = " of PiSpeedtest is available. You have version: "
    newversionmessage3 = " installed."
    lookingforupdateserror = "An error occured while looking for updates."
    skipdetected = "SKIP DETECTED"
    speedtestconfignotfound = "Could not find the configuration file."
    loadingconfigurationmessage = "Loading configuration..."
    languageconfigurationnotfound = "Could not find the language configuration file."
    configurationfilealert = "ALERT: CONFIGURATION FILES ARE IN BETA. MODE SELECTION IS NOT INTEGRATED INTO THE APPLICATION YET!"
    configuredmodemessage = "The configured mode is: "
    minutes = " minutes."
    configuredspeedtestdurationmessage = "Configured speedtest duration: "
    invalidmode = "The speedtest file contains an invalid mode."
    invalidduration = "The speedtest file contains an invalid speedtest duration."
    configuredruneverysecondmessage = "Configured \"run every ___ seconds\": "
    runeverysecondinvalid = "The \"run every ___ seconds\" configuration is invalid."
else:
    pretestresults = "The current language configuration is somehow invalid."
    pretestresults2 = "The current language configuration is somehow invalid."
    nointernetconnectionmessage = "The current language configuration is somehow invalid."
    lookingforupdatesmessage = "The current language configuration is somehow invalid."
    latestversionmessage = "The current language configuration is somehow invalid."
    youhavethelatestversionmessage = "The current language configuration is somehow invalid."
    initialspeedtestinformation = "The current language configuration is somehow invalid."
    speedtestran = "The current language configuration is somehow invalid."
    speedtestseconds = "The current language configuration is somehow invalid."
    programmodes = "The current language configuration is somehow invalid."
    stablemode = "The current language configuration is somehow invalid."
    betamode = "The current language configuration is somehow invalid."
    compatiblemode = "The current language configuration is somehow invalid."
    pleaseselectaspeedtestmodemessage = "The current language configuration is somehow invalid."
    programdurationseconds = "The current language configuration is somehow invalid."

    programdurationminutes = "The current language configuration is somehow invalid."
    howofteninput = "The current language configuration is somehow invalid."
    seconds = "The current language configuration is somehow invalid."
    speedtestfilenameinput = "The current language configuration is somehow invalid."
    errormessage = "The current language configuration is somehow invalid."
    startingspeedtestmessage = "The current language configuration is somehow invalid."
    speedtestcompletedmessage = "The current language configuration is somehow invalid."
    programdurationmodemessage = "The current language configuration is somehow invalid."
    programdurationmodeerror = "The current language configuration is somehow invalid."
    newversionmessage = "The current language configuration is somehow invalid."
    newversionmessage2 = "The current language configuration is somehow invalid."
    newversionmessage3 = "The current language configuration is somehow invalid."

    lookingforupdateserror = "The current language configuration is somehow invalid."
    skipdetected = "The current language configuration is somehow invalid."
    speedtestconfignotfound = "The current language configuration is somehow invalid."
    loadingconfigurationmessage = "The current language configuration is somehow invalid."
    configurationfilealert = "The current language configuration is somehow invalid."
    configuredmodemessage = "The current language configuration is somehow invalid."

    minutes = "The current language configuration is somehow invalid."
    configuredspeedtestdurationmessage = "The current language configuration is somehow invalid."
    invalidmode = "The current language configuration is somehow invalid."
    invalidduration = "The current language configuration is somehow invalid."
    configuredruneverysecondmessage = "The current language configuration is somehow invalid."
    runeverysecondinvalid = "The current language configuration is somehow invalid."
#Main speedtest code:
def processpeedtest(backupmode, filename):
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    results = s.results.dict()
    resultlist = list(results.values())
    download = str(round(resultlist[0]/1000000)) + " mbit/s"
    upload = str(round(resultlist[1]/1000000)) + " mbit/s"
    ping = str(resultlist[2]) + "ms"
    downloadlist.append(download)
    uploadlist.append(upload)
    pinglist.append(ping)
    fullresults = "Results: " + " Download: " + download + " Upload: " + upload + " Ping: " + ping + "."
    print(fullresults)
    if backupmode == False:

        with open(filename, "a+") as file:
            file.write(fullresults + "\n")
    elif backupmode == True:
        with open("speedtestbackup.txt") as backupfile:
            backupfile.write(fullresults + "\n")
#(end of main speedtest code.)
try:
    request = requests.get("https://www.google.com")
    print(pretestresults + str(request.elapsed.total_seconds()) + pretestresults2)
except requests.exceptions.ConnectionError:
    print(nointernetconnectionmessage)

    noconnection = 1
print(lookingforupdatesmessage)
print("\n")
try:
    from bs4 import BeautifulSoup
    updatecheck = requests.get("https://pispeedtestfiles.000webhostapp.com/latestversion.html")
    soup = BeautifulSoup(updatecheck.text, "html.parser")

    latestversionnumber = str(soup.get_text()).replace("\n", "")
    print(latestversionmessage + latestversionnumber + ".")
    if latestversionnumber == fileversionnumber:
        print(youhavethelatestversionmessage)
    else:
        print(newversionmessage + latestversionnumber + newversionmessage2 + fileversionnumber + newversionmessage3)
except:
    print(lookingforupdateserror)

print("\n")
print(initialspeedtestinformation)
initialspeedtestsfile = os.path.join(os.getcwd() + "/configurationfiles/" + "intialspeedtests.txt")
timeone = time.time()
if noconnection == 0:
    processpeedtest(0, filename = initialspeedtestsfile)
elif noconnection == 1:
    print(nointernetconnectionmessage)
speedtesttime = round(time.time() - timeone)
print(speedtestran + str(speedtesttime) + speedtestseconds)
print("\n")
print(programmodes)
print(betamode)
print(stablemode)
print(compatiblemode)
mode = input(pleaseselectaspeedtestmodemessage)
if mode == "BETA MODE":
    import ctypes

    print("\n")
    try:
        configurationfile = os.path.join(os.getcwd() + "/configurationfiles/config.txt")

        with open(configurationfile, "r+") as configurationsfile:
            print(loadingconfigurationmessage)
            print(configurationfilealert)
            configurationfilecontent = configurationsfile.read().splitlines()
            if configurationfilecontent[9] in allowedmodes:
                configuredmode = configurationfilecontent[9]
                print(configuredmodemessage + configuredmode + ".")
                loadconfig[0] = 1
            elif configurationfilecontent[9] == "-SKIP-":
                print(skipdetected)
                loadconfig[0] = 0
            else:
                print(invalidmode)

                loadconfig[0] = 0
            try:
                configuredspeedtestduration1 = int(configurationfilecontent[10])
                configuredspeedtestduration = int(configuredspeedtestduration1*60)
                print(configuredspeedtestdurationmessage + str(configuredspeedtestduration/60) + minutes)
                loadconfig[1] = 1
            except:
                if configurationfilecontent[10] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[1] = 0
                else:
                    print(invalidduration)
                    loadconfig[1] = 0
            try:
                configuredruneverysecond = int(configurationfilecontent[11])
                print(configuredruneverysecondmessage + str(configuredruneverysecond) + seconds)
                loadconfig[2] = 1
            except:
                if configurationfilecontent[11] == "-SKIP-":
                    print(skipdetected)
                    loadconfig[2] = 0
                else:
                    print(runeverysecondinvalid)
                    loadconfig[2] = 0
    except:
        print(speedtestconfignotfound)
        loadconfig[0] = 0
        loadconfig[1] = 0
        loadconfig[2] = 0
    print("\n")

    if loadconfig[1] == 0:
        programdurationmode = input(programdurationmodemessage)
        if programdurationmode == "MINUTES":
            times = int(input(programdurationminutes)*60)
        elif programdurationmode == "SECONDS":
            times = int(input(programdurationseconds))
        else:
            print(programdurationmodeerror)
            times = int(input(programdurationminutes)*60)
    else:
        times = configuredspeedtestduration
    if loadconfig[2] == 1:
        interval = configuredruneverysecond
    else:
        interval = int(input(howofteninput + str(speedtesttime) + seconds))
    inputfilename = str(input(speedtestfilenameinput))
    filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
    with open(filedirectory, "w") as file:
        file.close()
    repeat = round(times/(interval-speedtesttime))
    ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
    steps = int(times)
    if noconnection == 0:
        for speedtestindex in range(repeat):
            try:
                print(startingspeedtestmessage)
                processpeedtest(0, filename=inputfilename)
                print(speedtestcompletedmessage)
                time.sleep(interval-speedtesttime)
            except:
                ctypes.windll.user32.MessageBoxW(None, errormessage, "PiSpeedtest", 0)

                print(errormessage)

                #This is being added in a later release:
                #box = ctypes.windll.user32.MessageBoxW(None, "An error occured while running a speedtest. Would you like to try again? Everything will restart. The file with new speedtest data will be namned \"speedtestbackup.txt\".", "PiSpeedtest", 5)
                #if box == 1:
                    #print("Kör speedtest igen.")
                    #for speedtestindex in range(repeat):

                        #print("A speedtest is being started.")
                        #processpeedtest(0, filename="speedtestbackup.txt")
                        #print("A speedtest has been completed.")
                        #time.sleep(interval)
                #elif box == 2:
                    #print("Quitting PiSpeedtest because of an error.")
                #else:
                    #print("Quitting PiSpeedtest because of an error.")
    else:
        print(nointernetconnectionmessage)

elif mode == "STABLE":
    import ctypes

    programdurationmode = input(programdurationmodemessage)
    if programdurationmode == "MINUTES":
        times = int(input(programdurationminutes) * 60)
    elif programdurationmode == "SECONDS":
        times = int(input(programdurationseconds))
    else:
        print(programdurationmodeerror)
        times = int(input(programdurationminutes) * 60)

    interval = int(input(howofteninput + str(speedtesttime) + seconds))
    inputfilename = str(input(speedtestfilenameinput))
    filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
    with open(filedirectory, "w") as file:
        file.close()
    ctypes.windll.user32.MessageBoxW(None, startingspeedtestmessage, "PiSpeedtest", 0)
    repeat = round(times / (interval - speedtesttime))
    steps = int(times)
    if noconnection == 0:
        for speedtestindex in range(repeat):
            try:
                print(startingspeedtestmessage)
                processpeedtest(0, filename=inputfilename)
                print(speedtestcompletedmessage)
                time.sleep(interval - speedtesttime)
            except:

                print(errormessage)
elif mode == "COMPATIBLE":
    import ctypes

    programdurationmode = input(programdurationmodemessage)
    if programdurationmode == "MINUTES":
        times = int(input(programdurationminutes) * 60)
    elif programdurationmode == "SECONDS":
        times = int(input(programdurationseconds))
    else:
        print(programdurationmodeerror)
        times = int(input(programdurationminutes) * 60)

    interval = int(input(howofteninput + str(speedtesttime) + seconds))
    inputfilename = str(input(speedtestfilenameinput))
    filedirectory = os.path.join(os.getcwd() + "/speedtestresults/" + inputfilename + ".txt")
    with open(filedirectory, "w") as file:
        file.close()
    repeat = round(times / (interval - speedtesttime))
    steps = int(times)
    if noconnection == 0:
        for speedtestindex in range(repeat):
            try:
                print(startingspeedtestmessage)
                processpeedtest(0, filename=inputfilename)
                print(speedtestcompletedmessage)
                time.sleep(interval - speedtesttime)
            except:

                print(errormessage)
